#Author :afeng
#Time   :2018/5/29 12:41
import pymysql
db=pymysql.connect("149.28.110.56","root","wangafeng","test")

cursor=db.cursor()

cursor.execute("select * from user")

list=cursor.fetchall()

print(list)
#这他妈是个元组,不是列表
print(type(list))