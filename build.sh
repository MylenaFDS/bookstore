#!/usr/bin/env bash
set -o errexit  # Faz o script parar quando um comando falhar

echo "🔧 Instalando dependências com Poetry..."
poetry install --no-dev

echo "🗄️ Rodando migrations..."
poetry run python manage.py migrate --noinput

echo "📦 Coletando arquivos estáticos..."
poetry run python manage.py collectstatic --noinput

echo "✅ Build finalizado com sucesso."
