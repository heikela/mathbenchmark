import numpy as np

np.random.seed(123)
a = np.random.randn(1000, 1000).astype('float32')
b = np.random.randn(1000, 1000).astype('float32')
c = np.zeros([1000,1000]).astype('float32')


def multiply():
    np.dot(a, b, c)


if __name__ == "__main__":
    import timeit
    setup = "from __main__ import multiply"
    print(timeit.timeit("multiply()", setup=setup, number=1000))


print(c[100, 100])


import tensorflow
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())

ta = tensorflow.constant(a)
tb = tensorflow.constant(b)

# Create a session object
sess = tensorflow.Session()
result = tensorflow.matmul(ta, tb)
print (timeit.timeit("sess.run(result)", setup="import tensorflow; from __main__ import sess, ta, tb, result", number=1000))

print(sess.run(result[100,100]))
sess.close()

