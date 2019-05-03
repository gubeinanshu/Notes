
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 需要先安装 mysql for python
import MySQLdb

conn = MySQLdb.Connect(
                        host = '127.0.0.1',
                        port = 3306,
                        user = 'root',
                        passwd = 'root',
                        db = 'test',
                        charset = 'utf8'
                        )
cursor = conn.cursor()

sql = "select * from a"
sql_insert = "insert into a(name,class) values('woshi',100)"
sql_update = "update a set name='qq' where class=1"
sql_delete = "delete from a where class=2"
try:
    cursor.execute(sql_insert)
    #输出影响了几行
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    #提交后才进行数据库修改
    conn.commit()
except Exception as e:
    print e
    #回滚，执行出错不会进行修改提交，进行回滚
    conn.rollback()

"""
cursor.execute(sql)
print cursor.rowcount
'''
#循环输出
rs = cursor.fetchall()
for raw in rs:
    print raw'''
#获取一条
rs = cursor.fetchone()
print rs
#获取接下来的3条
rs = cursor.fetchmany(3)
print rs
#获取剩下的所有行
rs = cursor.fetchall()
print rs """


cursor.close()
conn.close()

```
