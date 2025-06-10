# Usa Python 3.13 (release candidate, necessário para seu pyproject)
FROM python:3.13-rc-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH"

# Instala dependências do sistema e o Poetry
RUN apt-get update && apt-get install --no-install-recommends -y \
        curl build-essential libpq-dev gcc libc-dev python3-pip \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version \
    && apt-get purge --auto-remove -y build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Copia o projeto inteiro (inclui README.md, manage.py, etc.)
COPY . .

# Instala as dependências principais
RUN poetry install --only main

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
