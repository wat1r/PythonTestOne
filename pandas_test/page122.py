# coding=utf-8
import pandas as pd
import numpy as np

pd.set_option('display.max_columns',130)

file_path = "IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# print(df.info())

# print(df.head(1))

#获取平均评分
print(df["Rating"].mean())

#导演的人数
# print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))

# #获取演员的人数
# temp_actors_list = df["Actors"].str.split(", ").tolist()
# actors_list = [i for j in temp_actors_list for i in j]
# actors_num = len(set(actors_list))
# print(actors_num)
