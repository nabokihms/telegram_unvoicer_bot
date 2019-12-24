Telegram Unvoicer Bot
=====================
This thing was created all because my wife love to send me voicemails over and over again, and often I cannot listen to them.

Info
----
Bot for decoding voicemail messages to text. Simply send a message with voicemail to the bot, and he will return the message in a text.

**For now supporting voicemail messages from:**
* WhatsApp _(format .opus)_
* Telegram _(format ogg-opus)_

Install and run on Ubuntu >= 16.04
---
Clone the repo.
```bash
git clone `repo link`
```
```bash
cd telegram_unvoicer_bot
```

Install the docker.  
https://docs.docker.com/install/linux/docker-ce/ubuntu/
 
Build the image:
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

The last thing to set up telegram webhooks. In the docker image, we already have some ready scripts for it.
```
telegram_unvoicer_bot_set_webhook // for setup the webhook
telegram_unvoicer_bot_get_webhook_info // for webhook info
```
