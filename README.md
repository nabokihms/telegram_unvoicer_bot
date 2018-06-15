telegram_unvoicer_bot
---
Бот, предназначеный для разбора голосовых сообщений. Просто перешлите сообщение,
и он отправит вам его в виде текста.

**На данный момент поддерживаются:**
* WhatsApp _(формат .opus)_

Установка и запуск на Ubuntu >= 16.04
---
Клонируем себе репозиторий.
```bash
git clone `ссылка на репозиторий`
```
```bash
cd telegram_unvoicer_bot
```
Копируем файл с примером настроек. 
```bash
cp telegram_unvoicer_bot/settings.py.example \
   telegram_unvoicer_bot/settings.py
```
Пишем в `telegram_unvoicer_bot/settings.py` свои `HOST_URL` и 
`TELEGRAM_BOT_API_KEY`.
 
 Далее генерируем самоподписные сертификаты командой 
 ```bash
 bash scripts/create_certs.sh
 ```
 Устанавливаем себе Докер. Например по этой инструкции.
 https://docs.docker.com/install/linux/docker-ce/ubuntu/
 
 После чего собираем и запускаем образ:
 ```bash
 docker image build \
    -t telegram_unvoicer_bot:v1 \
    ./
 ```
 ```bash
 docker run \
    -d \
    --name telegram_unvoicer_bot \
    -p 443:443 \
    telegram_unvoicer_bot:v1
 ```