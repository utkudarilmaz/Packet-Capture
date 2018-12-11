FROM alpine:latest

MAINTAINER S. Utku DARILMAZ <utkudarilmaz@gmail.com>

LABEL desription="hping3 tool building on Alpine:latest"
LABEL version="1.0"

ENV buildDir /root/hping3-20051105

WORKDIR /root

RUN wget http://www.hping.org/hping3-20051105.tar.gz && tar -xvzf hping3-20051105.tar.gz
WORKDIR /root/hping3-20051105
RUN pwd
RUN sed -i '12i \\t|| defined(__x86_64__) \\' bytesex.h

RUN apk add gcc gcc-objc make libpcap-dev tcl-dev

RUN cd $(buildDir)
RUN ln -s /usr/include/pcap-bpf.h /usr/include/net/bpf.h

RUN ./configure && make && make install 

