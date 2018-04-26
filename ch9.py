#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 0:19
# @Author  : Aries
# @Site    : 
# @File    : ch9.py
# @Software: PyCharm

#################       urllib        ##################
# import urllib.request as ur
#
# url = 'https://www.baidu.com'
# conn = ur.urlopen(url)  # conn httpresponse对象
# print(conn)
#
# data = conn.read()
# print(data)
# print(conn.status)
#
# print(conn.getheader('Content-Type'))  # 获取请求头中的数据格式
#
# # 响应中的各种HTTP头
# for key, value in conn.getheaders():
#     print(key, value)


##################        request        ###################
# import requests
# url = 'https://www.baidu.com'
# resp = requests.get(url)
# print(resp)
# print(resp.text)


##################       python web      ####################

# ##########      bottle      ###########
# from bottle import route,run
#
# @route('/')
# def home():
#     return "it is not fancy,but it is my home page"
# run(host='localhost',port=9999)

# from bottle import run,route,static_file
#
# @route('/')
# def home():
#     return static_file('index.html',root='.')
#
# @route('/echo/<thing>')
#
# def echo(thing):
#     return "say hello to %s!" % thing
# run(host='localhost',port=9999)


# ##########      flask       ###########

# from flask import Flask
#
# app = Flask(__name__,static_folder='.',static_url_path='')
#
# @app.route('/')
# def home():
#     return app.send_static_file('index.html')
#
# @app.route('/echo/<thing>')
# def echo(thing):
#     return "say hello to %s"%thing
#
# app.run(port=9999,debug=True)

# ###########     beautifulsoup     ########
def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        print('Links in',url)
        for num,link in enumerate(get_links(url),start=1):
            print(num,link)
        print()

