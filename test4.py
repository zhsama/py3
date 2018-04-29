#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 20:37
# @Author  : Aries
# @Site    : 
# @File    : test4.py
# @Software: PyCharm

# # 使用列表推导生成10以内（range(10)）偶数的列表
#
# lst = [number for number in range(10) if number % 2 == 0]
# print(lst)
#
# # 使用字典推导创建字典squares。把0~9内的整数作为键，每个键的平方作为对应的值。
#
# squ = {key: key * key for key in range(10)}
# print(squ)
#
# # 使用集合推导创建集合odd，包含0~9内（range(10)）的奇数。
# odd = {num for num in range(10) if num % 2 != 0}
# print(odd)
#
# # 用生成器推导返回字符串'Got '和0~9内的一个整数，使用for循环进行迭代。
# for thing in ('Got %s' % number for number in range(10)):
#     print(thing)
#
#
# # 定义一个生成器函数get_odds()：返回0~9内的奇数。使用for循环查找并输出返回的第三个值。
# def get_odds():
#     for num in range(1, 10, 2):
#         yield num
#
#
# # 定义一个装饰器test：当一个函数被调用时输出'start'，当函数结束时输出'end'。
# for number, count in enumerate(get_odds()):
#     if number == 2:
#         print(count)
#
#
# def test(func):
#     def new_func(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#
#     return new_func()
#
#
# @test
# def greeting():
#     print('greeting')
#
#
# greeting()

# 定义一个异常OopsException：编写代码捕捉该异常，并输出'Caught an oops'。
# class OopsException(Exception):
#     pass

# raise OopsException

# try:
#     raise OopsException
# except OopsException:
#     print('Caught an oops')

# 使用函数zip()创建字典movies：匹配两个列表titles  =  ['Creature  of  Habit', 'Crewel Fate']和plots = ['A nun turns into a monster', 'A haunted yarn shop']
# titles = ['Creature of Habit', 'Crewel Fate']
# plots = ['A nun turns into a monster', 'A haunted yarn shop']
#
# movies = dict(zip(titles,plots))
# print(movies)


