#!/bin/bash
set -Eeuo pipefail

hurl --continue-on-error --no-color tests_failed/runner_errors/runner_errors.hurl
