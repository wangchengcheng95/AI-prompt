# Refactor Plan: Image Parsing/Types/Config to Target Architecture (No Backward Compatibility)

## Summary

Implement a balanced architecture refactor that:
- keeps DTOs in `model` only,
- moves request parsing into a dedicated service parser module,
- removes `scanner` package type leakage by introducing shared engine input-domain types,
- replaces dynamic image gateway config parsing with typed config + strict fail-fast validation,
- updates code and docs in the same change.

This plan is strict (no legacy compatibility): old `scanners[].config.image_gateway` behavior is removed.

## Key Implementation Changes

1. Introduce shared engine input types (replace `scanner.Image`)
- Add new package `internal/enginev2/input` with:
  - `type ImageType string` (`url`, `base64`)
  - `type Image struct { Type ImageType; Content string }`
- Update usage sites to depend on `input.Image`:
  - `policy.DetectRequest.Images`
  - `policy.ExecutionContext.Images`
  - `scanner.ScanInput.Images`
  - `engine` content normalization/rate-limit path
  - service parser return type
- Remove image type definitions from `scanner` package to eliminate outward dependency leakage.

2. Service-layer parser module (DTO -> domain input)
- Extract parsing from `internal/service/guardrailv2.go` into `internal/service/guardrailv2_parser.go`.
- Keep parser in service layer, not `model`, with behavior unchanged from current rules:
  - `MultiPart` priority
  - `ContentType=2`: valid URL first, then Base64 image validation
  - invalid URL/non-image Base64 => `IMAGE_URL_INVALID`
  - oversize Base64 => `IMAGE_TOO_LARGE`
- `guardrailv2.go` only orchestrates request/response and calls parser helpers.

3. Typed image gateway config + strict fail-fast
- Add typed config to `EngineV2Config`:
  - `ImageGatewayConfig { Endpoint string; TimeoutMS int; MaxRetries int }` (under `enginev2.image_gateway`)
- Keep image scanner enable/stages in `enginev2.scanners[]`; remove gateway config consumption from `entry.Config`.
- Refactor `engine` scanner init wiring for image scanner to receive typed gateway config explicitly.
- Add strict validation:
  - if image scanner is enabled, `enginev2.image_gateway.endpoint` must be set and timeout/retry must be valid.
  - startup fails on invalid/missing image gateway typed config.
  - legacy `scanners[].config.image_gateway` is no longer recognized.

4. Docs and config alignment
- Update `docs/design/图片检测设计.md` to definitive typed config contract (`enginev2.image_gateway`) and updated boundaries.
- Update environment YAMLs (`dev`, `cn-beijing-6`, `cn-qingyangtest-1`) to new contract:
  - keep image scanner entry for enable/stages
  - move gateway fields to `enginev2.image_gateway`
  - remove scanner-local `image_gateway` block.

## Test Plan

1. Service parser tests
- Keep existing table tests and switch expected type imports to `input.ImageType`.
- Verify URL/Base64 edge cases and error-code behavior unchanged.

2. Config validation tests
- Add cases:
  - image scanner enabled + missing `enginev2.image_gateway.endpoint` => config validation error
  - valid typed gateway config => pass
  - invalid timeout/retry => validation error

3. Image scanner tests
- Refactor constructor tests to typed gateway config input path.
- Keep strict new gateway response-contract tests and fail-open observability assertions.

4. Regression tests
- Run targeted packages:
  - `internal/service`
  - `internal/enginev2/scanner/image`
  - `internal/enginev2/policy`
  - `internal/enginev2/pipeline`
  - `internal/pkg/metrics`
- Run same set with `-race`.

## Assumptions and Defaults

- Approved scope: minimal required cross-file set including code, impacted tests, and YAML/docs updates.
- No backward compatibility is required:
  - old scanner-local image gateway config is removed, not fallback-parsed.
- Keep generic scanner registry pattern; only image gateway configuration path is made typed and explicit.
