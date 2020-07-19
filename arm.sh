#!/bin/sh
docker build -t tftrt-demo -f Dockerfile.arm .
docker run --runtime nvidia --network host -it --rm tftrt-demo