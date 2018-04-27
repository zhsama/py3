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
# socket.getservbyname('http')
# socket.getservbyport(80)

######      email       ######
# 1.smtplib使用简单邮件传输协议发送邮件
# 2.email用来创建和解析邮件
# 3.poplib可以使用邮递协议（pop3）来读取邮件
# 4.imaplib可以使用因特网消息访问协议（imap）来读取邮件
# ---smtpd
# ---lamon

######      api       #######
# import requests
# url = "https://gdata.youtube.com/feeds/api/standerfeeds/top_rated?alt=json"
# response = requests.get(url)
# data = response.json()
# for video in data['feed']['entry'][0:6]:
#     print(video['title']['$t'])

###############     远程处理        ################
# from xmlrpc.server import SimpleXMLRPCServer
#
#
# def double(num):
#     return num * 2
#
# server = SimpleXMLRPCServer(("localhost",6789))
# server.register_function(double,"double")
# server.serve_forever()

###############      msg pcr python      #############
# from msgpackrpc import Server, Address
# class Services():
#     def double(self,num):
#         return num * 2
#
# server = Server(Services())
# server.listen("localhost",6789)
# server.start()

# #############      fabric       #############
#
# def iso():
#     from datetime import date
#     print(date.today().isoformat())
# --------------------------------------------------
# from fabric.api import local
#
# def iso():
#     local('date -u')
# --------------------------------------------------
# from fabric.api import run
# from fabric.context_managers import env
#
# env.password = "your password goes here"
#
# def iso():
#     run('date -u')
# ---------------------------------------------------
# from fabric.api import run
#
# def iso():
#     run('date -u')
