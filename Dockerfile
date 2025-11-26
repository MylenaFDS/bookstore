FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.4

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    curl build-essential libpq-dev gcc git \
    && curl -sSL https://install.python-poetry.org | python3 -

# Adicionar Poetry no PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copiar arquivos do Poetry
COPY pyproject.toml poetry.lock ./

# Desativar virtualenv e instalar dependências no sistema
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copiar o projeto
COPY . .

# Criar pasta de estáticos
RUN mkdir -p /app/staticfiles

# Coletar estáticos
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Render vai usar isso automaticamente
CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000"]

