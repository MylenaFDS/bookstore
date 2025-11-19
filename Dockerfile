# Etapa base
FROM python:3.12-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/opt/poetry/bin:$PATH"

# Instalar dependências
RUN apt-get update && apt-get install -y curl build-essential libpq-dev gcc git \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version

# Criar diretório e copiar dependências
WORKDIR /app
COPY pyproject.toml poetry.lock ./

# Instalar dependências de runtime
RUN poetry install --no-dev

# Copiar o projeto
COPY . .

# Coletar arquivos estáticos
RUN poetry run python manage.py collectstatic --noinput

# Expor porta do Django
EXPOSE 8000

# Comando de inicialização
CMD ["poetry", "run", "gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000"]

