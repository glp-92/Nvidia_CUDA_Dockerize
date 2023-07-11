import tensorflow as tf

def get_tf_version():
    return f"Tensorflow version: {tf.__version__}. GPU name: {tf.config.experimental.get_device_details(tf.config.list_physical_devices('GPU')[0])['device_name']}"