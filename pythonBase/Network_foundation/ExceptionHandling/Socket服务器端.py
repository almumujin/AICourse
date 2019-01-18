import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # AF_INET:基于网络通信 SOCK_STREAM:基于TCP(基于流式通信)协议
phone.bind(('127.0.0.1', 8000))  # 类似绑定手机卡

phone.listen(5)  # 代表可以有几个电话等着接受
conn, addr = phone.accept()  # 等电话  拿到电话链接和对方手机号

msg = conn.recv(1024)  # 代表收到1024字节信息
print('客户端发来的消息：', msg)


conn.send(msg.upper())  # 发消息

conn.close()  # 挂电话
phone.close()  # 关机
