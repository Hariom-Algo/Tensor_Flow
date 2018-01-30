import tensorflow as tf

a = tf.constant(6.5, name='constant_a')
b = tf.constant(3.4,name='constant_b')
c = tf.constant(3.0,name='constant_c')
d = tf.constant(100.2, name = 'constant_d')


square = tf.square(a,name="square_a")
power  = tf.pow(b,c,name="pow_b_c")
sqrt   = tf.sqrt(d,name="sqrt_d")

final_sum = tf.add_n([square,power,sqrt],name = "final_computation")

sess = tf.Session()

print(sess.run(square))
print(sess.run(power))
print(sess.run(sqrt))
print(sess.run(final_sum))
another_sum = tf.add_n([a,b,c,d,power],name="another_sum")
another_sum_2 = tf.add_n([a,b,sqrt],name="sqrt_sum")
writer = tf.summary.FileWriter('./m2_example2',sess.graph)
writer.close()
sess.close()

