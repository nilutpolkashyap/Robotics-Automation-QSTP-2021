# import tensorflow as tf

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# tf.test.is_gpu_available(
#     cuda_only=False, min_cuda_compute_capability=None
# )

# gpu_available = tf.test.is_gpu_available()
# print("Value : ", gpu_available)

# from tensorflow.python.client import device_lib

# def get_available_gpus():
#     local_device_protos = device_lib.list_local_devices()
#     return [x.name for x in local_device_protos if x.device_type == 'GPU']

# get_available_gpus()

import tensorflow as tf
from tensorflow.python.client import device_lib

local_device_protos = device_lib.list_local_devices()

gpu_count = len(tf.config.list_physical_devices('GPU'))

print("***************************************************************")

if( gpu_count > 0):
    print("GPU Detected")
    print("Available number of GPU Devices : {}".format(gpu_count))
else:
    print("No GPU Detected")

print("***************************************************************")

# local_device_protos = device_lib.list_local_devices()
if (gpu_count):
    for x in local_device_protos:
        if x.device_type == 'GPU':
            print(x.physical_device_desc)