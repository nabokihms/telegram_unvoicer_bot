Voice to text bot
=====================

Motivation
----------
This bot was created because my wife loved sending me voicemails instead of typing, and I was too busy talking with my colleagues to listen to them. Without ensuring there was nothing urgent happened, I couldn't just ignore them.

How does it work?
-----------------
If you send a voicemail to the bot, and he will extract a text from it.
* Click on a message with a voicemail.
* Click `Share`.
* Choose `Telegram` and click on this bot icon (you can create your own bot using @botfather).
* Wait for the text.

**Supported audio formats:**
* WhatsApp _(format .opus)_
* Telegram _(format ogg-opus)_

Build and Deploy
----------------
 
Build the docker image using your TELEGRAM_API_KEY:
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

The last thing left is setting up telegram webhooks. In the previously created docker image, we already have some ready scripts for it.
```
telegram_unvoicer_bot_set_webhook // for setup the webhook
telegram_unvoicer_bot_get_webhook_info // for webhook info
```
