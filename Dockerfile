FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЮ папку proxy как есть
COPY proxy ./proxy

# Копируем secret.txt
COPY secret.txt ./secret.txt

ENV PYTHONPATH=/app

RUN useradd -m -u 1000 proxyuser && chown -R proxyuser:proxyuser /app
USER proxyuser

EXPOSE 8444

# Запускаем как модуль из папки proxy
CMD ["sh", "-c", "cd /app/proxy && python tg_ws_proxy.py --host 0.0.0.0 --port ${PORT:-8444} --secret $(cat /app/secret.txt)"]
