import tensorflow as tf

x = tf.placeholder(tf.int32,shape=[3], name ='x')
y = tf.placeholder(tf.int32,shape=[3],name='y')

sum_x = tf.reduce_sum(x,name="sum_x")
prod_y = tf.reduce_prod(y,name="prod_y")


final_dev  =  tf.div(sum_x,prod_y,name="final_dev")
final_mean = tf.reduce_mean([sum_x,prod_y],name="final_mean")

sess = tf.Session()

print('sum(x)',sess.run(sum_x,feed_dict = {x : [100,200,300]}))
print('prod_y',sess.run(prod_y,feed_dict = {y : [100,200,300]}))

print('sum(x)/prod_y',sess.run(final_dev,feed_dict = {x : [100,200,300],y : [100,200,300]}))

writer =  tf.summary.FileWriter('./m3_example1',sess.graph)
writer.close()

sess.close()