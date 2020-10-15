import numpy as np
import pandas as pd

a = np.array([1,2,3], ndmin=3)
b = np.array([[[2, 4, 3], [2, 4, 3]]])
print(np.ndim(b))
print(np.shape(b))
b.shape = (3,2)
c = b.reshape(2,3)
print(c)
print(b)
# print(np.itemsize(b))
c = np.arange(20)
print(c)

# print(a)

emptya = np.empty((3,1), dtype= [('name', 'S20'), ('age', 'i4')])
print("empty", emptya)
zerosa = np.zeros((3,2))
print(zerosa)
onesa = np.ones((3,2))
print(onesa)

a = [1,2]
b = np.asarray(a)
print(b)

# shape reshape size ravel flattenb

# a = np.array(["zhangsan", 12, "nan"], ["lisi", 13, "nv"])
# b = list(a)
c = [["zhangsan", 12, "nan"], ["lisi", 13, "nv"]]
d = pd.DataFrame(c, columns=["姓名", "年龄", "性别"])
print(d)

import os
print(os.getcwd())
os.chdir(r"C:\Users\ERIC\Desktop\python")

date1 = pd.read_csv("date1.csv")
# help(pd.read_csv)
# print(date1)
# print(date1.dtypes)
# print(date1.head(1))
# print(pd.__version__)
print("-------------------")
date1 = pd.read_excel("date1.xlsx", sheet_name="Sheet2")
sheet_name = ["Sheet" + str(i) for i in range(1, 3)]
print(sheet_name)
# print(date1)

date_all = pd.DataFrame()
for i in sheet_name:
    data = pd.read_excel("date1.xlsx", sheet_name=i)
    date_all = pd.concat([date_all, data], axis=0)
print(date_all)
print(os.getcwd())
date_all.to_csv("date1_save.csv")
date_all.to_excel("date1_save.xlsx")