#!/usr/bin/env bash
set -o errexit

# Ensure commands run where manage.py and pyproject.toml live.
cd mysite

./build.sh
