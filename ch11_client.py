#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 18:04
# @Author  : Aries
# @Site    : 
# @File    : ch11_client.py
# @Software: PyCharm

#######################         并发网络        ############################


##############      请求--响应对       ################
# import zmq
#
# host = '127.0.0.1'
# port = 6789
# context = zmq.Context()
# client = context.socket(zmq.REQ)
# client.connect("tcp://%s:%s" % (host,port))
# for num in range(1,6):
#     request_str = "message #%s" % num
#     request_bytes = request_str.encode('utf-8')
#     client.send(request_bytes)
#     reply_bytes = client.recv()
#     reply_str = reply_bytes.decode('utf-8')
#     print("Sent %s, received %s" % (request_str, reply_str))

#############       RPC       ################

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789")
num = 7
result = proxy.double(num)

print("Double %s is %s" % (num,result))