#!/usr/bin/env bash
set -o errexit

pip install poetry

# Instalar dependências diretamente no ambiente do Render
poetry config virtualenvs.create false

poetry install --no-interaction --no-ansi

python manage.py collectstatic --noinput
python manage.py migrate



