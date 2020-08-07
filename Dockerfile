FROM alpine:latest

RUN apk add python3 python3-dev py3-pip
RUN pip3 install flask

COPY . /opt

WORKDIR /opt

CMD ["/usr/bin/python3", "app.py"]



