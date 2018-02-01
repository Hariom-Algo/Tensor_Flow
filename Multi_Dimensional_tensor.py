import tensorflow as tf

x = tf.constant([100,200,300] , name='x')
y = tf.constant([1,2,3] , name='y')

sum_x = tf.reduce_sum(x,name="sum_x")
prod_y = tf.reduce_prod(y,name="prod_y")

final_dev  =  tf.div(sum_x,prod_y,name="final_dev")
final_mean = tf.reduce_mean([sum_x,prod_y],name="final_mean")

sess = tf.Session()
print('x',sess.run(sum_x))
print('y',sess.run(prod_y))
print('final_dev',sess.run(final_dev))
print('final_mean',sess.run(final_mean))

writer = tf.summary.FileWriter('./m2_example4',sess.graph)
writer.close()

sess.close()