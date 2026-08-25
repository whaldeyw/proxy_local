TG MTProto WS Bridge Proxy
Прокси для Telegram MTProto через WebSocket с поддержкой Cloudflare.

Быстрый запуск через Docker
1. Скачайте репозиторий
text
git clone https://github.com/whaldeyw/proxy_local.git
cd tg-proxy
2. Создайте файл с секретом
text
echo "ваш_секрет_здесь" > secret.txt
Секрет должен быть 32 символа в шестнадцатеричном формате. Можно сгенерировать командой:

text
openssl rand -hex 16
3. Запустите
text
docker-compose up -d
4. Проверьте логи
text
docker-compose logs -f
В логах вы увидите ссылку для подключения в Telegram:

text
tg://proxy?server=IP_вашего_сервера&port=8444&secret=ddВАШ_СЕКРЕТ
5. Остановка
text
docker-compose down
6. Перезапуск после изменений
text
docker-compose down
docker-compose build --no-cache
docker-compose up -d
Запуск без Docker
Установка зависимостей
text
pip install -r requirements.txt
Запуск
text
cd proxy
python tg_ws_proxy.py --host 0.0.0.0 --port 8444 --secret $(cat ../secret.txt)
Или с автоматической генерацией секрета:

text
python tg_ws_proxy.py --host 0.0.0.0 --port 8444
Важно
После запуска найдите в логах ссылку для подключения

Ссылка имеет формат: tg://proxy?server=IP&port=8444&secret=ddСЕКРЕТ

Скопируйте эту ссылку и откройте в Telegram

Telegram автоматически настроит подключение

