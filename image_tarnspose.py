import tensorflow as tf
import matplotlib.image as mp_img
import matplotlib.pyplot as plot
import os


filename  = "C:\\Users\\hsingh\\Desktop\\Tensor_Flow\\hariom.jpg"
image  =  mp_img.imread(filename)
print("Image shape",image.shape)
print("Image array",image)
plot.imshow(image)
plot.show()

x = tf.Variable(image,name='x')
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # Original Axis Indexes 0,1,2
    # We are swapping it to 1,0,2 the first and second axis is swapped
    #transpose = tf.transpose(x,perm=[1,0,2])

    # Better way to do the transpose
    transpose = tf.image.transpose_image(x)
    result = sess.run(transpose)
    print("Transposed image shape",result.shape)
    plot.imshow(result)
    plot.show()











