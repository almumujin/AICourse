import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买手机

phone.connect(('127.0.0.1', 8000))  # 拨通电话 电话号为对方绑定的元组

phone.send('hello'.encode('utf-8'))  # 收发消息基于二进制 跟网络间传输信息方式一致
data = phone.recv(1024)
print('收到服务端发来的消息:', data)
