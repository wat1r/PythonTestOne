import numpy as np

input_path="./test_one.csv"

# t1 = np.loadtxt(input_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(input_path,delimiter=",",dtype="int" )

# print(t1)
# print("*"*50)
print(t2)
print(t2[[0,1]])







