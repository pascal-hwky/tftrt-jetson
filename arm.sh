#!/bin/sh
sudo docker build -t tftrt-demo -f Dockerfile.arm .
sudo docker run --runtime nvidia --network host -it --rm tftrt-demo