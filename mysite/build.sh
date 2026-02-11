#!/usr/bin/env bash
set -o errexit

pip install poetry -U
poetry install --only main --no-root

python manage.py collectstatic --no-input

python manage.py migrate