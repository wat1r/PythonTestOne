import numpy as np
import random

t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

t3 = np.arange(4, 10, 2)
print(t3)

print(t3.dtype)

print("-" * 50)

t4 = np.array(np.arange(1, 4), dtype=float)
print(t4)
print(t4.dtype)

print("-" * 50)
t5 = np.array([1, 1, 0, 1, 0, 0], dtype=bool)
print(t5)
print(t5.dtype)

print("-" * 50)
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

print("-" * 50)
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

print("-" * 50)
t8 = np.round(t7,2)
print(t8)