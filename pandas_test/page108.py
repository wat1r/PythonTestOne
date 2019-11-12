# coding=utf-8
import pandas as pd

# pandas读取csv中的文件
df = pd.read_csv("./dogNames2.csv")

# print(df)

print(df[(df["Count_AnimalName"] > 800 )& (df["Count_AnimalName"] < 1000)])

# print(df[(800<df["Count_AnimalName"])|(df["Count_AnimalName"]<1000)])
