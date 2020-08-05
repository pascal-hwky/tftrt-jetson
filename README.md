# TF-TRT demo

This demo application shows how to create a simple Keras model and optimize it using the TF-TRT runtime on the Jetson platform.

## Running on Jetson Nano with JetPack 4.4:

Flash a Jetson Nano with JetPack 4.4 by following the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write). Log in and run the following commands:

```
git clone https://github.com/pascal-hwky/tftrt-jetson.git
cd tftrt-jetson
./arm.sh
```

## Running on development PC:

If you want to make changes to the code while testing in a Docker container on a development PC, run the following command:

```
./dev.sh
```

This command will map the current directory to `/shared/` in the container. To run the code, execute the following command in the container:

```
python3 main.py
```
