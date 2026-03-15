#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST_PATH="${ROOT_DIR}/references/repos.manifest.tsv"

if [[ ! -f "${MANIFEST_PATH}" ]]; then
  echo "Manifest not found: ${MANIFEST_PATH}" >&2
  exit 1
fi

usage() {
  cat <<'EOF'
Usage:
  scripts/sync-references.sh
  scripts/sync-references.sh --only <name>
  scripts/sync-references.sh --manifest <path>

Behavior:
  - Clone a reference repository if the local checkout is missing
  - Pull with --ff-only if the local checkout already exists
EOF
}

ONLY_NAME=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --only)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --only" >&2
        usage
        exit 1
      fi
      ONLY_NAME="$2"
      shift 2
      ;;
    --manifest)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --manifest" >&2
        usage
        exit 1
      fi
      MANIFEST_PATH="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ ! -f "${MANIFEST_PATH}" ]]; then
  echo "Manifest not found: ${MANIFEST_PATH}" >&2
  exit 1
fi

matched=0
synced=0

while IFS=$'\t' read -r name repo_url branch local_path; do
  if [[ -z "${name}" || "${name}" == \#* ]]; then
    continue
  fi

  if [[ -n "${ONLY_NAME}" && "${name}" != "${ONLY_NAME}" ]]; then
    continue
  fi

  matched=1
  target_dir="${ROOT_DIR}/${local_path}"

  echo "==> ${name}"
  echo "    repo:   ${repo_url}"
  echo "    branch: ${branch}"
  echo "    path:   ${local_path}"

  mkdir -p "$(dirname "${target_dir}")"

  if [[ -d "${target_dir}/.git" ]]; then
    git -C "${target_dir}" fetch origin "${branch}"
    git -C "${target_dir}" checkout "${branch}"
    git -C "${target_dir}" pull --ff-only origin "${branch}"
  elif [[ -e "${target_dir}" ]]; then
    echo "Target exists but is not a git checkout: ${local_path}" >&2
    exit 1
  else
    git clone --branch "${branch}" "${repo_url}" "${target_dir}"
  fi

  synced=$((synced + 1))
  echo
done < "${MANIFEST_PATH}"

if [[ "${matched}" -eq 0 ]]; then
  echo "No matching references found in ${MANIFEST_PATH}" >&2
  exit 1
fi

echo "Synced ${synced} reference repository(s)."
