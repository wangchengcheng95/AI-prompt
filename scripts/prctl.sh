#!/usr/bin/env bash

set -euo pipefail

program_name() {
  printf '%s\n' "${PRCTL_INVOKED_AS:-$0}"
}

usage() {
  local program
  program="$(program_name)"

  cat <<EOF
Usage:
  ${program} push --branch <branch>
  ${program} find-head --head <branch>
  ${program} create --base <base> --head <branch> --title <title> --body-file <path> [--draft]
  ${program} edit --pr <number> [--title <title>] [--body-file <path>]
  ${program} view --pr <number>

Behavior:
  - Wrap the small set of git and gh commands used for repo-local pull request work
  - Keep PR operations bundled with the skill so the workflow migrates as one unit
EOF
}

die() {
  echo "$*" >&2
  exit 1
}

require_arg() {
  local flag="$1"
  local value="${2:-}"
  [[ -n "${value}" ]] || die "Missing value for ${flag}"
}

ensure_gh() {
  command -v gh >/dev/null 2>&1 || die "gh is required but not installed"
}

ensure_file() {
  local path="$1"
  [[ -f "${path}" ]] || die "File not found: ${path}"
}

repo_selector() {
  local repo remote_url host path trimmed

  repo="${GH_REPO:-${GITHUB_REPOSITORY:-}}"
  if [[ -n "${repo}" ]]; then
    printf '%s\n' "${repo}"
    return
  fi

  remote_url="$(git remote get-url origin 2>/dev/null)" || die "origin remote is required to resolve the repository slug"

  case "${remote_url}" in
    git@*:* )
      trimmed="${remote_url#git@}"
      host="${trimmed%%:*}"
      path="${trimmed#*:}"
      ;;
    ssh://git@*/*)
      trimmed="${remote_url#ssh://git@}"
      host="${trimmed%%/*}"
      path="${trimmed#*/}"
      ;;
    https://*/*)
      trimmed="${remote_url#https://}"
      host="${trimmed%%/*}"
      path="${trimmed#*/}"
      ;;
    http://*/*)
      trimmed="${remote_url#http://}"
      host="${trimmed%%/*}"
      path="${trimmed#*/}"
      ;;
    *)
      die "Could not parse origin remote into a GitHub repository slug: ${remote_url}"
      ;;
  esac

  path="${path%.git}"
  [[ "${path}" == */* ]] || die "Could not parse origin remote into owner/repo: ${remote_url}"

  if [[ "${host}" == "github.com" ]]; then
    printf '%s\n' "${path}"
  else
    printf '%s/%s\n' "${host}" "${path}"
  fi
}

cmd="${1:-}"
if [[ -z "${cmd}" ]]; then
  usage
  exit 1
fi
shift

case "${cmd}" in
  push)
    branch=""
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --branch)
          require_arg "$1" "${2:-}"
          branch="$2"
          shift 2
          ;;
        -h|--help)
          usage
          exit 0
          ;;
        *)
          die "Unknown argument for push: $1"
          ;;
      esac
    done

    require_arg "--branch" "${branch}"
    git push -u origin "${branch}"
    ;;

  find-head)
    head=""
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --head)
          require_arg "$1" "${2:-}"
          head="$2"
          shift 2
          ;;
        -h|--help)
          usage
          exit 0
          ;;
        *)
          die "Unknown argument for find-head: $1"
          ;;
      esac
    done

    require_arg "--head" "${head}"
    ensure_gh
    gh pr list --head "${head}" --state all --json number,title,url,state,isDraft,baseRefName,headRefName
    ;;

  create)
    base=""
    head=""
    title=""
    body_file=""
    draft=0

    while [[ $# -gt 0 ]]; do
      case "$1" in
        --base)
          require_arg "$1" "${2:-}"
          base="$2"
          shift 2
          ;;
        --head)
          require_arg "$1" "${2:-}"
          head="$2"
          shift 2
          ;;
        --title)
          require_arg "$1" "${2:-}"
          title="$2"
          shift 2
          ;;
        --body-file)
          require_arg "$1" "${2:-}"
          body_file="$2"
          shift 2
          ;;
        --draft)
          draft=1
          shift
          ;;
        -h|--help)
          usage
          exit 0
          ;;
        *)
          die "Unknown argument for create: $1"
          ;;
      esac
    done

    require_arg "--base" "${base}"
    require_arg "--head" "${head}"
    require_arg "--title" "${title}"
    require_arg "--body-file" "${body_file}"
    ensure_gh
    ensure_file "${body_file}"

    args=(
      gh pr create
      --base "${base}"
      --head "${head}"
      --title "${title}"
      --body-file "${body_file}"
    )

    if [[ "${draft}" -eq 1 ]]; then
      args+=(--draft)
    fi

    "${args[@]}"
    ;;

  edit)
    pr_number=""
    title=""
    body_file=""

    while [[ $# -gt 0 ]]; do
      case "$1" in
        --pr)
          require_arg "$1" "${2:-}"
          pr_number="$2"
          shift 2
          ;;
        --title)
          require_arg "$1" "${2:-}"
          title="$2"
          shift 2
          ;;
        --body-file)
          require_arg "$1" "${2:-}"
          body_file="$2"
          shift 2
          ;;
        -h|--help)
          usage
          exit 0
          ;;
        *)
          die "Unknown argument for edit: $1"
          ;;
      esac
    done

    require_arg "--pr" "${pr_number}"
    [[ -n "${title}" || -n "${body_file}" ]] || die "edit requires --title and/or --body-file"
    ensure_gh

    repo="$(repo_selector)"
    args=(gh api --repo "${repo}" "repos/{owner}/{repo}/pulls/${pr_number}" -X PATCH)

    if [[ -n "${title}" ]]; then
      args+=(-f "title=${title}")
    fi

    if [[ -n "${body_file}" ]]; then
      ensure_file "${body_file}"
      body="$(<"${body_file}")"
      args+=(-f "body=${body}")
    fi

    "${args[@]}"
    ;;

  view)
    pr_number=""
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --pr)
          require_arg "$1" "${2:-}"
          pr_number="$2"
          shift 2
          ;;
        -h|--help)
          usage
          exit 0
          ;;
        *)
          die "Unknown argument for view: $1"
          ;;
      esac
    done

    require_arg "--pr" "${pr_number}"
    ensure_gh
    gh pr view "${pr_number}" --json number,title,url,state,baseRefName,headRefName
    ;;

  -h|--help)
    usage
    exit 0
    ;;

  *)
    die "Unknown command: ${cmd}"
    ;;
esac
