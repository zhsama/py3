#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 17:47
# @Author  : Aries
# @Site    : 
# @File    : ch11.py
# @Software: PyCharm

#######################         并发网络        ############################


##############      请求--响应对   P252-253     ################
# import zmq
#
# host = '127.0.0.1'
# port = 6789
# context = zmq.Context() # 能保存状态的ZeroMQ对象
# server = context.socket(zmq.REP) # REQ  用于响应
# server.bind("tcp://%s:%s" % (host, port)) # 监听指定端口
#
# while True:
#     # 等待client的下一个请求
#     request_bytes = server.recv()
#     request_str = request_bytes.decode('utf-8') # 字符串转换成utf-8编码 decode 文本字符串和字节字符串的转换
#     print("qq%s" % request_str)
#     replay_str = "22%s" % request_str
#     replay_bytes = bytes(replay_str, 'utf-8')
#     server.send(replay_bytes)


###############     网络服务        ################

######      域名系统        ######
import socket
# print(socket.gethostbyname_ex('www.baidu.com'))
# print(socket.getaddrinfo('www.baidu.com',443))# 查找ip地址 返回信息全 可用于创建套接字连接
# print(socket.getaddrinfo('www.baidu.com',443,socket.AF_INET,socket.SOCK_STREAM)) # 只获取tcp或者udp的内容
socket.getservbyname('http')
socket.gets







