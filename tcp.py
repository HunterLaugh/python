# coding: utf-8

# 引入socket
import socket

# AF_INET使用IPv4协议 ，创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接，参数是tuple
s.connect(('www.sina.com.cn',80))

# 发送数据
s.send(b' GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

# 接收数据
buffer=[]
while True:
	# 每次最多接收1k字节
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data=b''.join(buffer)

s.close()

# 接收到的数据写入文件，分离HTTP头和网页，HTTP打印出来，网页内容保存到文件
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

with open('sina.html','wb') as f:
	f.write(html)