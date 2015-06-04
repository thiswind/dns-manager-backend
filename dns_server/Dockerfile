FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y -q wget
RUN wget -q -O - "$@" http://git.io/vkiUF | bash -s --
