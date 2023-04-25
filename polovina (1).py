import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return 2 * np.sin(x) - np.tan(x)

def max_value_on_interval(a, b, epsilon):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) < f(b):
            a = c
        else:
            b = c
    return (a + b) / 2


a = 0
b = np.pi / 4
epsilon = 0.05


max_x = max_value_on_interval(a, b, epsilon)
max_value = f(max_x)

print("Максимальное значение функции:", max_value)
print("Точка x с максимальным значением:", max_x)



