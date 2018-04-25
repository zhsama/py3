#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 1:51
# @Author  : Aries
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm


##################################   xml 处理   ###########################
# import xml.etree.ElementTree as et
#
# tree = et.ElementTree(file='menu.xml')
#
# root = tree.getroot()
#
# print(root.tag)
#
# for child in root:
#     print('tag:',child.tag,'attributes:', child.attrib)
#     for grandchild in child:
#         print(grandchild.tag,grandchild.attrib)


############################# json 处理 #########################
################    字典《==》json互换    ################
# menu = {
#     "breakfast":{
#         "hours":"7-11",
#         "items":{
#             "breakfast burritos":"$6.00",
#             "pancake":"$4.00"
#         }
#     },
#     "lunch":{
#         "hours":"11-3",
#         "items":{
#             "hamburgers":"$5.00"
#         }
#     },
#     "dinner":{
#         "hours":"3-10",
#         "items":{
#             "spaghetti":"$8.00"
#         }
#     }
# }
#
# import json
# menu_json = json.dumps(menu)
# # print(menu_json)
# menu2 = json.loads(menu_json)
# print(type(menu2))
# print(menu2)


################    对象《==》json互换    ##############
# import datetime,json
# now = datetime.datetime.utcnow()
# # print(now)
# # json.dumps(now)   无法打印对象 需要转换
# now_str = str(now)
# json.dumps(now_str)
# from time import mktime
# now_epoch = int(mktime(now.timetuple()))
# json.dumps(now_epoch)
#


########################   yaml ####################################
# import yaml
# with open('test.yaml','rt') as fin:
#     text = fin.read()
#
# data = yaml.load(text)
# print(data['details'])
#
# print(len(data['poems']))


#######################     sqlite    ################################
# import sqlite3
# conn = sqlite3.connect('test.db')
# curs = conn.cursor()
# # curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY ,count INT,damages FLOAT)''')   #创建表
# # curs.execute('''insert into zoo values ("duck",5,0.0)''')     #对表zoo进行insert操作
# # curs.execute('''insert into zoo values ("bear",2,1000.0)''')
# #########       placeholder插入数据     ###########
# # ins = 'insert into zoo(critter,count,damages) values(?,?,?)'
# # curs.execute(ins,('weasel',1,2000.0))
# #########       select查表        #########
# # curs.execute('select * from zoo')  #####order by 排序   order by 表名 desc(倒叙)
# # rows = curs.fetchall()
# # print(rows)
# #########       关闭连接       #########
# curs.close()
# conn.close()


#######################     mysql       #############################


#######################     postgresql       #############################


#######################     sqlalchemy       #############################
# import sqlalchemy as sa
#
# conn = sa.create_engine('sqlite://')
# conn.execute('''CREATE TABLE test (critter VARCHAR(20) PRIMARY KEY ,count INT,damages FLOAT)''')
# ins = 'insert into test(critter, count, damages) values(?,?,?)'
# conn.execute(ins,'duck',5,0.0)
# conn.execute(ins,'bear',2,1000.0)
# conn.execute(ins,'weasel',1,2000.0)
# ins = 'insert into test(critter, count, damages) values(?,?,?)'
# rows = conn.execute('select * from test')
# for row in rows:
#     print(row)
#
# print(type(rows))


#############       sqlalchemy的sql操作函数      ###############
# import sqlalchemy as sa
#
# conn = sa.create_engine('sqlite://')
# meta = sa.MetaData()    #创建数据源
# test = sa.Table('test', meta,
#                 sa.Column('critter', sa.String, primary_key=True),
#                 sa.Column('count', sa.Integer),
#                 sa.Column('damages', sa.Float)
#                 )
# meta.create_all(conn)
#
# conn.execute(test.insert(('bear',5,0.0)))
# conn.execute(test.insert(('duck',8,1000.0)))
# conn.execute(test.insert(('weasel',2,2000.0)))
#
# result = conn.execute(test.select())
# rows = result.fetchall()
# print(rows)


#############       sqlalchemy ORM      ###############
# import sqlalchemy as sa
# from sqlalchemy.ext.declarative import declarative_base
#
# conn = sa.create_engine('sqlite:///zoo.db')
# Base = declarative_base()
#
#
# class Zoo(Base):
#     __tablename__ = 'zoo'
#     critter = sa.Column('critter', sa.String, primary_key=True)
#     count = sa.Column('count', sa.Integer)
#     damages = sa.Column('damages', sa.Float)
#
#     def __init__(self, critter, count, damages):
#         self.critter = critter
#         self.count = count
#         self.damages = damages
#
#     def __repr__(self):
#         return "<Zoo({},{},{})>".format(self.critter, self.count, self.damages)
#
#
# Base.metadata.create_all(conn)  # 创建数据库和表单
# first = Zoo('duck', 10, 0.0)
# second = Zoo('bear', 1, 1000.0)
# third = Zoo('damages', 2, 2000.0)
# from sqlalchemy.orm import sessionmaker  # ORM接触sql 创建会话session
#
# Session = sessionmaker(bind=conn)
# session = Session()
# session.add(first)  # 添加单一对象
# session.add_all([second, third])  # 添加一个列表的对象
# session.commit()


######################        dbm family        #################
# import dbm
# db = dbm.open('definitions','c')
# db['mustard'] = 'yellow'
# db['ketchup'] = 'red'
# db['pesto'] = 'green'
#
# # print(len(db))
# # print(db['mustard'])
# db.close()
# db = dbm.open('definitions','r')
# print(db['pesto'])


######################        memcached        ###################
# import memcache
# db = memcache.Client(['127.0.0..1:11211'])
# db.set('marco','polo')
# db.get('marco')


#####################         Redis       ####################
import redis

conn = redis.Redis()

# print(conn.keys('*'))

##########      单个字符串赋值取值       ############
# conn.set('secret', 'ni!')
# conn.set('carats', 24)
# conn.set('fever', '101.5')
# print(conn.get('secret'))
# print(conn.get('carats'))
# print(conn.get('fever'))
#
# conn.setnx('secret', 'new!')  # 当键值不存在的时候方可赋值 setnx
# print(conn.get('secret'))
#
# conn.getset('secret', 'new!-new!-new!-new!')  # 返回旧值 传入新值 getset
#
# print(conn.getrange('secret', -6, -1))  # 得到对应子串 0开始 -1结束 getrange
#
# conn.setrange('secret', 0, 'new?old!')  # 替换子串 从开始位置偏移 setrange
# print(conn.get('secret'))

##########      多个字符串取值赋值       ############
# conn.mset({'pie':'cherry','cordial':'sherry'})
#
# conn.mget('fever','carats')
#
# conn.delete('fever') # 删除字段
# ##########      增加/减少值
# print(conn.incr('carats'))  # 默认增加值为1
# print(conn.decr('carats'))  # 默认减少值为1
#
# print(conn.incrbyfloat('fever', -2.0))  # 默认增加值为1 不存在在decrbyfloat 可用负数代替

#############       列表        #############
# 第一次插入数据时创建列表
# conn.lpush('zoo', 'bear')  # 从开始处插入
# conn.lpush('zoo', 'bear', 'duck')  # 插入多个数据
#
# conn.linsert('zoo', 'before', 'duck', 'duck0')  # 在数据前插入数据
# conn.linsert('zoo', 'after', 'duck', 'duck1')  # 在数据后插入数据
#
# conn.lset('zoo', 2, 'marmoset')  # 在偏移量处插入数据 列表必须已存在
#
# conn.rpush('zoo', 'yak')  # 结尾处插入
#
# conn.lindex('zoo', 3)  # 取偏移量处的值
#
# print(conn.lrange('zoo', 0, -1))  # 取偏移量范围的值
# print(conn.lrange('zoo', 0, 1))  # 取特定偏移量的值
#
# conn.ltrim('zoo',0,-1)#保留列表中范围内的值

##########    哈希表(仅包含字符串 只有一层结构 不能嵌套)     #############
# conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})  # 设置多个字段
#
# conn.hset('song', 'mi', 'a note to follow re')  # 设置单一字段
#
# conn.hget('song', 'do')  # 获取一个字段
#
# conn.hmget('song', 're', 'mi')  # 获取多个字段
#
# conn.hkeys('song')  # 获取所有字段的键
#
# conn.hvals('song')  # 获取所有字段的值
#
# conn.hgetall('song')  # 获取哈希表所有键值

##########        集合        ###########
# conn.sadd('zoo1', 'duck', 'goat', 'turkey')  # 添加一个或多个值
#
# conn.scard('zoo1')  # 获取集合值的数量
#
# conn.smembers('zoo1')  # 获取集合中所有值
#
# # conn.srem('zoo')#删除集合中的值（一个/多个）
# #####    集合间的操作    ####
# conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')
#
# conn.sinter('zoo1', 'better_zoo')  # 返回两个集合之间的交集
# conn.sinterstore('fowl_zoo', 'zoo1', 'better_zoo')  # 储存集合之间的交集到新的集合
#
# conn.sunion('zoo1', 'better')  # 并集
# conn.sinterstore('fabu_zoo', 'zoo1', 'better_zoo')  # 储存并集到新集合
#
# conn.sdiff('zoo1', 'better_zoo')  # 获取差值
# conn.sdiffstore('zoo_sale', 'zoo1', 'better_zoo')  # 获取差值并储存到新集合

##########        有序集合        ###########
# 特点：
# 1.值独一无二
# 2.每个值关联对应浮点值分数（score）
#
# 作用：
# 1.排行榜
# 2.二级索引
# 3.时间序列
import time

now = time.time()
# print(now)
# conn.zadd('logins','smeagol',now)#新增访客
# conn.zadd('logins','sauron',now+(5*60))
# conn.zadd('logins','bilbo',now+(2*60*60))
# conn.zadd('logins','treebeard',now+(24*60*60))
# conn.zrank('logins', 'bilbo')  # 登录顺序
# print(conn.zscore('logins', 'bilbo'))  # 登陆时间
#
# print(conn.zrange('logins', 0, -1))  # 按登录顺序查看
#
# print(conn.zrange('logins',0,-1,withscores=True))#附带score

#########        位图        ##########
# 特点：
# 1.省空间
# 2.快速
# 3.处理超大集合数字

days = ['2018-04-25', '2018-04-26', '2018-04-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212
#
# conn.setbit(days[0], big_spender, 1)#设置登录
# conn.setbit(days[0], tire_kicker, 1)
# conn.setbit(days[1], big_spender, 1)
# conn.setbit(days[2], big_spender, 1)
# conn.setbit(days[2], late_joiner, 1)
# 统计日访问数
# for day in days:
#     print(conn.bitcount(day))

# conn.getbit(days[1],tire_kicker) #当日是否访问








