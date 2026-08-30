FROM python:3.10-slim

LABEL maintainer="Oleg"
LABEL description="Telegram MTProto WS Bridge Proxy"

WORKDIR /app

# Копируем и устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем папку proxy
COPY proxy ./proxy
COPY entrypoint.py ./entrypoint.py

ENV PYTHONPATH=/app

RUN useradd -m -u 1000 proxyuser && chown -R proxyuser:proxyuser /app
USER proxyuser

ENTRYPOINT ["python3", "/app/entrypoint.py"]