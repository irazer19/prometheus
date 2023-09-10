FROM ubuntu:latest
LABEL authors="irazer19"

RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz
RUN tar xvfz node_exporter-*.*-amd64.tar.gz
# RUN cd node_exporter-*.*-amd64
EXPOSE 9100

CMD node_exporter-*.*-amd64/node_exporter