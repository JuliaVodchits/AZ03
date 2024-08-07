# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y)

plt.title("Диаграмма рассеяния для двух наборов случайных данных")

plt.xlabel("ось X")
plt.ylabel("ось Y")

plt.show()