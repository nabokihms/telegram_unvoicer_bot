Telegram Unvoicer Bot
=====================

Motivation
----------
This thing exists only because my wife loves sending me voicemails over and over again. Without headphones, I have no chance to ensure whether this message is urgent or not. Fortunately, this bot works like a charm for me. He is the savior of my marriage.

How does it work?
-----------------
Send a voicemail to the bot, and he will extract a text from it.
* Click on a message with a voicemail
* Click `Share`
* Choose `Telegram` and click on this bot icon
* Wait for the text

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
