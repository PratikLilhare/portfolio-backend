FROM python:3.9

WORKDIR /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false

COPY ./app/pyproject.toml ./app/poetry.lock* /app/

RUN poetry install --no-root --only main

COPY ./app /app
ENV PYTHONPATH=/app

EXPOSE 8080

CMD uvicorn --reload --host "0.0.0.0" --port 80 --forwarded-allow-ips "*" "app.main:app"



