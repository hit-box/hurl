#!/bin/bash
set -Eeuo pipefail

hurl --continue-on-error tests_failed/assert_variable/assert_variable.hurl
