#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 22:02
# @Author  : Aries
# @Site    : 
# @File    : ch9_flask.py
# @Software: PyCharm




from flask import  Flask,render_template

app = Flask(__name__)

@app.route('/echo/thing')
def echo(thing):
    return render_template('index.html',thing=thing)

app.run(port=9999,debug=True)

