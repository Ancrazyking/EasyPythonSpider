#Author :afeng
#Time   :2018/5/29 12:16
import sqlite3

if __name__=="__main__":
    conn=sqlite3.connect("test.db")
    #创建游标
    c=conn.cursor()
    #创建一个user表
    c.execute("create table user(user_id INTEGER,user_name TEXT,user_sex INTEGER,user_age INTEGER,user_create TEXT)")
    #插入数据
    c.execute("insert into user(user_id,user_name,user_sex,user_age,user_create) values(?,?,?,?,datetime('now'))",(1,'python',1,3))
    #提交事务
    conn.commit()
    #关闭连接
    conn.close()