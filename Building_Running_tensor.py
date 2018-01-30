import tensorflow as tf

# Immutable constants
a = tf.constant(6,name='constant_a')
b = tf.constant(3,name='contant_b')
c = tf.constant(10,name='contant_c')
d = tf.constant(5,name='contant_d')

mul = tf.multiply(a,b,name='mul')
div = tf.div(c,d,name="div")

# Output of the multiplication what needs to be added
addn = tf.add_n([mul,div],name="addn")

# Print out the result
print (addn)

# Strange Output
# Wanted the value of addin after it has performed
# all the computation
# Tensor("addn:0", shape=(), dtype=int32)

"""
Printing data just gives the name of the Tensor ,shape and its data type
doesn't give  value it hold anypoint of time
This is because above code is not run
It has just constructed the Graph in tensorflow but haven't executed to get the result
To Execute it session is required  
"""
sess = tf.Session()
print(sess.run(addn))

# a*b + c/d = 6*3 + 10/5 = 18 + 2 = 20

writer = tf.summary.FileWriter('./m2_example1',sess.graph)
writer.close()
sess.close()
# Command to be used
# tensorboard --logdir="m2_example1"
