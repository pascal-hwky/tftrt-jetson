#!/bin/sh
docker build -t tftrt-demo -f Dockerfile.dev .
docker run --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 --gpus all -it --rm -v $PWD:/shared/ tftrt-demo