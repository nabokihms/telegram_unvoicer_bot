FROM alpine:3.7
LABEL telegram_unvoicer_bot="0.0.1"

ENV PATH=/usr/local/bin:$PATH \
    LANG=C.UTF-8

COPY . /telegram_unvoicer_bot

RUN apk add --update \
        python3 python3-dev \
        gcc g++ make libffi-dev openssl-dev \
        sox \
        opus-tools \
        nginx \
    && pip3 install ./telegram_unvoicer_bot \
    && apk del \
        python3-dev \
        gcc g++ make libffi-dev openssl-dev \
    && rm -rf /var/cache/apk/ \
    && rm -rf ~/.cache/pip\
    && cp \
        /telegram_unvoicer_bot/nginx/nginx.conf /etc/nginx/conf.d/default.conf \
    && mkdir /tmp/documents \
    && mkdir /run/nginx \
    && chmod 755 /telegram_unvoicer_bot/scripts/*

EXPOSE 80 443

CMD [ "/telegram_unvoicer_bot/start.sh" ]
