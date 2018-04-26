#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 21:42
# @Author  : Aries
# @Site    : 
# @File    : ch9_test.py
# @Software: PyCharm


import requests

resp = requests.get('http://localhost:9999/echo/zhcf')
# print(resp.status_code)
if resp.status_code == 200 and \
    resp.text == 'say hello to zhcf!':
        print('it is working!')
else:
    print('oops..')