
FROM python:3.12-slim

WORKDIR /app

COPY src/ ./src/

RUN mkdir -p /app/data

CMD ["python", "-m", "src.main"]
