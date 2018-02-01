# Numpy array can be treated as tensor
# How to use or convert numpy array to tensor

import tensorflow as tf
import numpy as np


# Tensorflow and numpy are tightly integrated
# Tensorflow data types are based on those from numpy

print (np.int32 == tf.int32)

sess = tf.Session()
zeroD  =  np.array(30,dtype=np.int32)
print(sess.run(tf.rank(zeroD)))
print(sess.run(tf.shape(zeroD)))

oneD = np.array([5.6,6.3,8.9,9.0],dtype=np.float32)
print(sess.run(tf.rank(oneD)))
print(sess.run(tf.shape(oneD)))



