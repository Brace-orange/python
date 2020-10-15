import os
import pandas as pd
import numpy as np

os.chdir(r"C:\Users\ERIC\Desktop\python")
date1 = pd.read_excel("date1_save.xlsx")
date1.head(3)
date1.tail(3)
print("columns:" + date1.columns)
print("dtypes:")
print(date1.dtypes)
print(date1.size)
print(date1)
print("-----筛选")
print(date1[:2])
print(date1[1:])

print(date1.姓名)
print(date1["年龄"])
print(date1[["姓名", "年龄"]])
print(date1.loc[1:2,:])