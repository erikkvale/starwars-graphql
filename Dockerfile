FROM python:3.9.4-alpine

WORKDIR /usr/src/app/

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Install OS dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev \
        libffi-dev \
        gcc \
        # https://github.com/psycopg/psycopg2/issues/684#issuecomment-392015532
        postgresql-dev \
        musl-dev \
        python3-dev \
        curl

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /usr/src/app/

RUN poetry install --no-root --no-dev

COPY . /usr/src/app/