# TF-TRT demo

This demo application shows how to create a simple Keras model and optimize it using the TF-TRT runtime on the Jetson platform.

## Running on Jetson Nano with JetPack 4.4:

Flash a Jetson Nano with JetPack 4.4 by following the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write). Log in and run the following commands:

```
git clone https://github.com/pascal-hwky/tftrt-jetson.git
cd tftrt-jetson
./arm.sh
```

**Note**: the TensorRT optimization step currently fails with the following message:

```
E tensorflow/compiler/tf2tensorrt/utils/trt_logger.cc:42] DefaultLogger ../builder/symbolicDims.cpp (625) - Assertion Error in fromSymbolic: 0 (x must be build-time constant)
W tensorflow/compiler/tf2tensorrt/kernels/trt_engine_op.cc:1002] Engine creation for PartitionedCall/TRTEngineOp_0 failed. The native segment will be used instead. Reason: Internal: Failed to build TensorRT engine
```

However, the inference will continue to run.

## Running on development PC:

If you want to make changes to the code while testing in a Docker container on a development PC, run the following command:

```
./dev.sh
```

This command will map the current directory to `/shared/` in the container. To run the code, execute the following command in the container:

```
python3 main.py
```
