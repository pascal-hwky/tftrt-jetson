"""
Keras model in TF2 and optimized inference using TF-TRT runtime.
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.compiler.tensorrt import trt_convert as trt

def get_model():
    """
    Simple model for TF-TRT runtime demo purpose only
    """
    inputs = keras.Input(shape=(32,))
    outputs = keras.layers.Dense(1)(inputs)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mean_squared_error")
    return model

# Create and save model
# See https://www.tensorflow.org/guide/keras/save_and_serialize
model = get_model()
model.save('model')

# Test 1: load model in TF
loaded_model = keras.models.load_model('model')

# Test 2: create TensorRT inference graph
# See https://docs.nvidia.com/deeplearning/frameworks/tf-trt-user-guide/index.html#worflow-with-savedmodel
conversion_params = trt.DEFAULT_TRT_CONVERSION_PARAMS
conversion_params = conversion_params._replace(
    max_workspace_size_bytes=(1<<32))
conversion_params = conversion_params._replace(precision_mode="FP16")
conversion_params = conversion_params._replace(
    maximum_cached_engiens=100)

converter = trt.TrtGraphConverterV2(
    input_saved_model_dir='model',
    conversion_params=conversion_params)
converter.convert()
def my_input_fn():
  for _ in range(100):
    inp1 = np.random.normal(size=(8, 32)).astype(np.float32)
    inp2 = np.random.normal(size=(8, 32)).astype(np.float32)
    yield inp1#, inp2
converter.build(input_fn=my_input_fn).converter.save('model-tftrt')

saved_model_loaded = tf.saved_model.load(
    'model-tftrt', tags=[tf.compat.v1.saved_model.tag_constants.SERVING])
graph_func = saved_model_loaded.signatures[
    tf.compat.v1.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
frozen_func = tf.python.framework.convert_to_constants.convert_variables_to_constants_v2(
    graph_func)

input_data = np.random.normal(size=(8, 32)).astype(np.float32)
output = frozen_func(input_data)[0].numpy()
