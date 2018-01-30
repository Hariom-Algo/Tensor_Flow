import tensorflow as tf
hello =  tf.constant('Hello , TensorFlow world!')
sess = tf.Session()
print(sess.run(hello))

