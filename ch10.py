#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 23:53
# @Author  : Aries
# @Site    : 
# @File    : ch10.py
# @Software: PyCharm

################################         systerm        ######################################

###############       file        ###############
# fout = open('ooops.txt','wt')
# print('oooops!!',file=fout)

import os

# print(os.path.exists('ooops.txt'))#判断文件是否存在
#
# print(os.path.exists('./ooops.txt'))

##############      程序和进程       ##############
# print(os.getpid())  # 获取当前进程号
# print(os.getcwd())  # 获取当前工作目录
# os.getuid() # 获取用户id
# print(os.getgid()) # 获取用户组id

#####   subprocess创建进程    #####
import subprocess
# ret = subprocess.getoutput('date -u')
# print(ret)
#
# ret = subprocess.getoutput('date -u | wc')
# print(ret)
#
# ret = subprocess.check_output(['date','-u']) # 不调用shell
# print(ret)
#
# ret = subprocess.getstatusoutput('date') # 获取退出状态 返回元组
# print(ret)

# ret = subprocess.call('date') # 获取退出状态

# ret = subprocess.call(['date','-u']) # 不调用shell

#####   multiprocessing    #####
# import multiprocessing
# import os
#
# def do_this(what):
#     whoami(what)
#
# def whoami(what):
#     print('Process %s says: %s' % (os.getpid(),what))
#
# if __name__ == "__main__":
#     whoami("the main process")
#     for n in range(4):
#         p = multiprocessing.Process(target=do_this  ,
#                                     args=("function %s" % n,))
#         p.start()

############    终止进程    ################

# import multiprocessing
# import time
# import os
#
# def whoami(name):
#     print("I'm %s, in process %s" % (name, os.getpid()))
#
# def loopy(name):
#     whoami(name)
#     start = 1
#     stop = 1000000
#     for num in range(start, stop):
#         print("\tNumber %s of %s. Honk!" % (num, stop))
#         time.sleep(1)
#
# if __name__ == "__main__":
#     whoami("main")
#     p = multiprocessing.Process(target=loopy, args=("loopy",))
#     p.start()
#     time.sleep(5)
#     p.terminate()

# ++