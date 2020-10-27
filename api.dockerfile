FROM python:3.8-buster

LABEL maintainer="Matt Love <matt@stellar.tech>"

RUN apt-get update && \
    apt-get install -y \
    build-essential

COPY . /responder
WORKDIR /responder/

RUN pip install --no-cache-dir --requirement requirements.txt

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 8080

CMD ["/start.sh"]
