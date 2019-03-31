FROM alpine:3.9
LABEL telegram_unvoicer_bot="0.0.1"

ENV PATH=/usr/local/bin:$PATH \
    LANG=C.UTF-8

COPY . /telegram_unvoicer_bot

RUN apk add --update \
    python3 python3-dev \
    gcc g++ make libffi-dev openssl-dev \
    sox \
    opus-tools \
    && pip3 install ./telegram_unvoicer_bot \
    && apk del \
    python3-dev \
    gcc g++ make libffi-dev openssl-dev \
    && rm -rf /var/cache/apk/ \
    && rm -rf ~/.cache/pip\
    && mkdir /tmp/documents && mkdir /tmp/music

EXPOSE 80 443

CMD [ "/bin/sh", "/telegram_unvoicer_bot/start.sh" ]
