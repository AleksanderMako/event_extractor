FROM ubuntu:20.04

# Setup python and java and base system
ENV DEBIAN_FRONTEND noninteractive
ENV LANG=en_US.UTF-8

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -q -y openjdk-8-jdk python3-pip libsnappy-dev language-pack-en supervisor

RUN pip3 install --upgrade pip requests

ADD supervisord.conf /etc/supervisor/supervisord.conf
RUN apt-get update \ 
&& apt-get -y install wget
RUN pip3 install giveme5w1h
RUN apt-get -y install zip unzip
RUN giveme5w1h-corenlp install

EXPOSE 9000
CMD [ "giveme5w1h-corenlp" ]