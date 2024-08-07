import numpy as np
import matplotlib.pyplot as plt

def array_examples():
    a = np.array([1, 2, 3, 4])
    print(a)
    b = np.zeros((3, 3))
    print(b)
    c = np.ones((2, 5))
    print(c)
    d = np.random.random((3, 5))
    print(d)
    e = np.arange(0, 10, 2)
    print(e)
    f = np.linspace(0, 13, 10)
    print(f)

def exercise_1():
    x = np.linspace(-10, 10, 100)
    y = x**2

    plt.plot(x, y)

    plt.title("График ф-ии y=x**2")

    plt.xlabel("ось X")
    plt.ylabel("ось Y")
    plt.grid(True)

    plt.show()


# array_examples()
# exercise_1()