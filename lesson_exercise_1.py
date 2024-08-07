import matplotlib.pyplot as plt

def exercise_1():
    x = [2, 6, 8, 14, 20]
    y = [6, 4, 10, 12, 16]

    plt.plot(x, y)

    plt.title("Пример простого линейного графика")

    plt.xlabel("ось X")
    plt.ylabel("ось Y")

    plt.show()

def exercise_2():
    data = [1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 8]

    plt.hist(data, bins=6)

    plt.title("Пример гистограммы")

    plt.xlabel("ось X")
    plt.ylabel("ось Y")

    plt.show()

def exercise_3():
    data = [5, 6, 8, 8, 9, 6, 8, 6, 6, 9, 10, 8, 8, 7, 7, 7, 6, 9, 7, 7, 8, 8, 11]

    plt.hist(data)

    plt.title("Гисторгамма количества часов сна")

    plt.xlabel("ось X")
    plt.ylabel("ось Y")

    plt.show()

def exercise_4():
    x = [1, 4, 6, 7]
    y = [3, 5, 8, 10]

    plt.scatter(x, y)

    plt.title("Пример диаграммы рассеивания")

    plt.xlabel("ось X")
    plt.ylabel("ось Y")

    plt.show()

exercise_4()