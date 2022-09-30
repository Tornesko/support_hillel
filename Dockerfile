FROM --platform=linux/x86_64 python:3.10-slim

# Receive build arguments
ARG PIPENV_EXTRA_ARGS


# Change working directory
WORKDIR /app/


# Copy project files
COPY ./ ./


# Install deps
RUN pip install pipenv \
    && pipenv install --system --deploy --ignore-pipfile $PIPENV_EXTRA_ARGS


CMD sleep 3 \
    && python src/manage.py migrate \
    && gunicorn src.config.wsgi:application --bind 0.0.0.0:80
