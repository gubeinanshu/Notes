
```python

import socket

#创建socket对象
#AP_INET或AP_UNIX
#SOCK_STREAM tcp/ip SOCK_DGRAM udp
s = socket.socket(socket.AP_INET,socket.SOCK_STREAM)
#绑定端口
s.bind(('127.0.0.1',8125))
#n代表循序多少个同时请求
socket.listen(8)

while 1:
    connection,address = s.accept()
    buf = connection.recv(10) #接收多少数据
    connection.send(buf) #返回数据
s.close() #关闭连接


```








