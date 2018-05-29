#Author :afeng
#Time   :2018/5/29 12:30
import sqlite3
conn=sqlite3.connect("./test.db")
#获取游标
c=conn.cursor()
#操作数据库,获取结果集
c.execute("select * from user")
result=c.fetchall()
conn.close()
print(result)
print(type(result))