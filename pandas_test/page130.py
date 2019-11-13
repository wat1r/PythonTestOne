# coding=utf-8
import pandas as pd
import numpy as np

file_path = "./starbucks_store_worldwide.csv"
pd.set_option('display.max_columns',130)

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())
grouped = df.groupby(by="Country")
print(grouped)

# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j)
#     print("*" * 100)

#DataFrameGroupBy
#可以进行遍历
# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j,type(j))
#     print("*"*100)
# df[df["Country"]="US"]
#调用聚合方法

# print(grouped["Brand"].count())

# country_count = grouped["Brand"].count()
# print(country_count["US"])
# print(country_count["CN"])
# country_count = grouped["Brand"].count()
# print(country_count["US"])
# print(country_count["CN"])

# china_data = df[df["Country"] == "CN"]
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
#
# print(grouped)


#统计中国每个省店铺的数量
# china_data = df[df["Country"] =="CN"]
#
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
#
# print(grouped)

# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped,type(grouped))


#数据按照多个条件进行分组,返回Series
# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)
# print(type(grouped))

#数据按照多个条件进行分组,返回DataFrame
grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
grouped2= df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
grouped3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]

# print(grouped1,type(grouped1))
# print("*"*100)
# print(grouped2,type(grouped2))
# print("*"*100)
# #
# print(grouped3,type(grouped3))

#索引的方法和属性
print(grouped1.index)
