FROM python:3.12.1-alpine3.18
RUN apk update && apk add vim tmux curl && mkdir -p /app
COPY . /app
RUN cd /app && pip3 install -r requirements.txt
WORKDIR /app
EXPOSE 5000
CMD ["/bin/sh","-c","while true;do sleep 10000;done"]
