TG MTProto WS Bridge Proxy
Прокси для Telegram MTProto

🐳 Docker-контейнер — быстрый запуск в изолированной среде

🔄 Автоматическое определение IP — работает на любом сервере

🏠 Локальный режим — для разработки и тестирования (127.0.0.1)

🌐 Серверный режим — автоматическое определение внешнего IP

🔐 Фиксированный секрет — через .env файл

📝 Настройка через переменные окружения — гибкая конфигурация

Быстрый запуск через Docker
1. Скачайте репозиторий

git clone https://github.com/whaldeyw/proxy_local.git

cd proxy_local

2. Настройте окружение

Отредактируйте файл .env:

nano .env

# Настройки прокси
PORT=1248                      # Порт для прокси
HOST=0.0.0.0                   # Хост (оставьте 0.0.0.0)
SECRET=2ba522c2a1d68eda0cc421bfb18cc826  # 32 символа hex

# Режим работы
LOCAL_MODE=false               # true - 127.0.0.1, false - внешний IP

# Внешний IP (опционально)
EXTERNAL_IP=                   # Оставьте пустым для автоопределения

# Настройки Docker
CONTAINER_NAME=tg-proxy
TIMEZONE=Europe/Moscow

Важно: Секрет должен быть 32 символа в шестнадцатеричном формате. Можно сгенерировать командой:

openssl rand -hex 16

3. Запустите

docker-compose up -d

4. Проверьте логи

docker-compose logs -f

В логах вы увидите ссылку для подключения в Telegram:

🔗 Connect:
  tg://proxy?server=IP_вашего_сервера&port=1248&secret=ddВАШ_СЕКРЕТ

5. Остановка

docker-compose down

6. Перезапуск после изменений

docker-compose down
docker-compose build --no-cache
docker-compose up -d

Управление режимами

Локальный режим (для разработки)

В .env установите:

LOCAL_MODE=true

Ссылка будет:

tg://proxy?server=127.0.0.1&port=1248&secret=ddВАШ_СЕКРЕТ

Серверный режим (автоопределение IP)

В .env установите:

LOCAL_MODE=false
EXTERNAL_IP=

IP определится автоматически через публичные сервисы (api.ipify.org).

Ручная установка IP

В .env укажите:
ваш ip принудительно, например 
EXTERNAL_IP=185.262.111.210

Будет использован указанный IP.

Запуск без Docker

Установка зависимостей

pip install -r requirements.txt

Запуск

cd proxy
python tg_ws_proxy.py --host 0.0.0.0 --port 1248 --secret $(cat ../secret.txt)

Или с автоматической генерацией секрета:

python tg_ws_proxy.py --host 0.0.0.0 --port 1248

Важно
После запуска найдите в логах ссылку для подключения

Ссылка имеет формат: tg://proxy?server=IP&port=1248&secret=ddСЕКРЕТ

Скопируйте эту ссылку и откройте в Telegram

Telegram автоматически настроит подключение

Полезные команды

docker-compose ps

Просмотр логов

docker-compose logs -f
docker-compose logs -n 50

Перезапуск с новым портом

В .env измените PORT:

PORT=8080

docker-compose down

docker-compose up -d

Смена секрета

В .env измените SECRET:

SECRET=новый_секрет_32_символа
docker-compose down
docker-compose up -d

Вход в контейнер

docker exec -it tg-proxy sh

Структура проекта

proxy_local/
├── .env                     # Переменные окружения
├── docker-compose.yml       # Docker Compose конфиг
├── Dockerfile               # Dockerfile
├── requirements.txt         # Python зависимости
├── entrypoint.py            # Точка входа (определение IP)
├── proxy/                   # Исходники прокси
│   ├── tg_ws_proxy.py
│   ├── utils.py
│   └── ...
└── secret.txt               # Секрет (опционально)

Ссылка для подключения

После запуска скопируйте ссылку из логов:

tg://proxy?server=YOUR_IP&port=1248&secret=ddYOUR_SECRET

