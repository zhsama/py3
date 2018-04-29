#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 19:59
# @Author  : Aries
# @Site    : 
# @File    : test3.py
# @Software: PyCharm


year_list = [1998, 1999, 2000, 2001, 2002, 2003]

# print(year_list[3])
#
# print(year_list[-1])

name = ['mozzarella', 'cinderella', 'salmonella']

# print(name)
# count = 0
# for n in name:
#     name[count] = name[count].capitalize()
#     print(name[count], 'up to', n)
#     count = count + 1
# print(len(name))
# for n in range(0,len(name)):
# num = 0
# while num<len(name):
#     for things in name:
#         name[num] = name[num].capitalize()
#         print(name[num])
#     num = num+1
# print(n)
# count1 = 0
# for n in name:
#     name[count] = name[count].upper()
#     print(name[count], 'up to', n)
#     count = count + 1


# e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
#
# print(e2f)
#
# print(e2f['cat'])
#
# print(e2f.items())
#
# f2e = {}
# for en, fn in e2f.items():
#     f2e[fn] = en

life = {
    'animals': {
        'cats': {
            'Henri': {}, 'Grumpy': {}, 'Lucy': {}
        },
        'octopi': {},
        'emus': {}
    },
    'plants': {

    },
    'other': {

    }
}

print(life.keys())
