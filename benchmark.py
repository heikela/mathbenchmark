import numpy as np

np.random.seed(123)
a = np.random.randn(200, 200)
b = np.random.randn(200, 200)
c = np.zeros([200,200])


def multiply():
    np.dot(a, b, c)


if __name__ == "__main__":
    import timeit
    setup = "from __main__ import multiply"
    print(timeit.timeit("multiply()", setup=setup, number=1000))


print(c[100, 100])
