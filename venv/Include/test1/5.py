import pymysql
from sqlalchemy import create_engine
import pandas as pd
import  os

conn = create_engine("mysql+pymysql://root:root@localhost:3306/test1")
sql = "select * from student"
pd1 = pd.read_sql(sql, conn)
print(pd1)

os.chdir(r"C:\Users\ERIC\Desktop\python")
dateall = pd.read_excel("date1_save.xlsx")
print(dateall)
conn1 = create_engine("mysql+pymysql://root:root@localhost:3306/test2")
try:
    dateall.to_sql("datesave", con=conn1, if_exists="replace",index=False)
    # dateall.to_sql
except:
    print("error")



