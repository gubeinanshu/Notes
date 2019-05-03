
python连接mysql
1. 需要先安装 mysql for python（百度搜索，自行解决）
2. 导入import MySQLdb

## mysqldb.connect(参数)
|参数名   |类型    |说明             |
|:-------:|:------:|:---------------:|
|host     |字符串  |MySQL服务器地址  |
|port     |数字    |MySQL服务器端口号|
|user     |字符串  |用户名           |
|passed   |字符串  |密码             |
|db       |字符串  |数据库名称       |
|charset  |字符串  |连接编码         |

## connection对象支持的方法

|方法名   |说明                    |
|:-------:|:---------------:       |
|host     |使用该连接创建并返回游标|
|port     |提交当前事物            |
|user     |回滚当前事物            |
|passed   |关闭连接                |

## DB API 数据库游标对象cursor
* 游标对象：用于执行查询和获取结果
* cursor对象支持的方法  

|参数名            |说明                                   |
|:----------------:|:-------------------------------------:|
|execute(op[,args] |执行一个数据查询和命令                 |
|fetchone()        |取的结果集的下一行                     |
|fetchmany(size)   |获取结果集的下几行                     |
|fetchall()        |获取结果集中剩下的所有行               |
|rowcount          |最近一次execute返回数据的行数或影响行数|
|close()           |关闭游标对象                           |
