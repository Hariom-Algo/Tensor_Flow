import tensorflow as tf

W = tf.Variable([2.5,4.0], tf.float32,name='var_W')
x = tf.placeholder(tf.float32,name='x')
b = tf.Variable([5.0,10.0], tf.float32,name='var_b')

y = W * x * b

# Initialize all variables defined
# Can't use variables without initialing them
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print("Final result wx + b",sess.run(y,feed_dict = {x: [10,100]}))


s = W * x

#Initialize only those variables that you might need
init = tf.variables_initializer([W])

with tf.Session() as sess:
    sess.run(init)
    #print("Final result wx + b",sess.run(y,feed_dict = {x: [10,100]}))
    print("Result : Wx=",sess.run(s,feed_dict={x:[10,100]}))




