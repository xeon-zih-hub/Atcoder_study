FROM python:3.12.13

ENV TZ=Asia/Tokyo
ENV TERM=xterm-256color

WORKDIR /work

RUN apt-get update && apt-get install -y \
    git \
    vim \
    curl \
    less \
    tree \
    procps \
    sudo \
    build-essential \
    && apt-get clean

RUN pip install --upgrade pip

RUN pip install \
    online-judge-tools

CMD ["bash"]
