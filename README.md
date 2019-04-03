telegram_unvoicer_bot
---
Бот, предназначеный для разбора голосовых сообщений. Просто перешлите сообщение,
и он отправит вам его в виде текста.

**На данный момент поддерживаются:**
* WhatsApp _(формат .opus)_
* Telegram _(формат ogg-opus)_

Установка и запуск на Ubuntu >= 16.04
---
Клонируем себе репозиторий.
```bash
git clone `ссылка на репозиторий`
```
```bash
cd telegram_unvoicer_bot
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
    -e TELEGRAM_API_KEY='your_key'
    --name telegram_unvoicer_bot \
    -p 8080:8080 \
    telegram_unvoicer_bot:v1
 ```

 Осталось настроить отправку вебхуков. В образе для этого есть несколько утилит.
 ```
 telegram_unvoicer_bot_set_webhook // для установки вебхука.
 telegram_unvoicer_bot_get_webhook_info // для просмотра информации.
 ```