import tensorflow as tf
sess = tf.Session()

zeroD = tf.constant(5)
print(sess.run(tf.rank(zeroD)))

my_str = "Hellow how are you"
OneD = tf.constant(my_str.split())
print(sess.run(tf.rank(OneD)))


#TwoD = tf.constant([[[]],[]])
TwoD = tf.constant([[1,2],[3,4]])
print(sess.run(tf.rank(TwoD)))

sess.close()