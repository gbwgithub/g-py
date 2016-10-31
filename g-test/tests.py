# coding=utf-8
# !/usr/bin/env python
#-------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------

















#-------------------------------------------------------------------------
# 直接创建数据库连接(不使用连接池)
#-------------------------------------------------------------------------
# import os
# import MySQLdb

# conn = MySQLdb.connect(host='127.0.0.1',
#                        user='jubao',
#                        passwd=os.environ.get('jubao_password'),
#                        db='jubao',
#                        port=3306,
#                        charset='utf8')
# conn.close()




#-------------------------------------------------------------------------
# 判断(__main__) , 调用main()格式 获取执行main()时抛出的异常,并记录
#-------------------------------------------------------------------------
# def main():
# 	import time
# 	raise Exception("抛出了一个自定义的异常\nraise a custom exception.\n" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#
# if __name__ == "__main__":
# 	try:
# 		main()
# 	except Exception as e:
# 		# 记录到日志 -> F:\Log\
# 		import time
# 		import os
# 		import traceback
#
# 		date_tag = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# 		log_file = 'F:' + os.sep + 'Log' + os.sep + os.path.basename(__file__) + date_tag + '.log'
# 		print(str(e) + '\n' + '记录到 -> ' + log_file)
# 		f = open(log_file, 'a')
# 		f.write(str(e) + '\n')
# 		f.close()
# 		traceback.print_exc()




#-------------------------------------------------------------------------
# python 读取环境变量
# 这里要理解的是，一个程序启动时，环境变量被复制到该程序所在的环境中，
# 在该程序执行过程中不会被除该程序以外的其他程序所改变。
# 
# so, 修改环境变量之后，如果受影响的是应用程序，那么只要简单地重新启动此应用程序，
# 环境变量的修改就会反映到该程序中，而不必重新启动计算机；
# 但是，如果受影响的是系统服务，就必须重新启动才能将环境变量的修改反映到系统服务中
# （因为没有办法在不重启计算机的情况下重新启动系统服务管理器）。
#-------------------------------------------------------------------------
# import os
# envVar = os.environ.get('path')
# jubaoPW = os.environ.get('jubao_password')
# abc = os.environ.get('abcxxx')	# 输出None
# print (envVar, jubaoPW, abc)







#-------------------------------------------------------------------------
# 获取系统分隔符 separator
#-------------------------------------------------------------------------
# import os
# print (os.sep)





#-------------------------------------------------------------------------
# 字符串切片 slice
#-------------------------------------------------------------------------
# str = '123456789'
# print(str[1:3] + 'gbw' + str[3:])





#-------------------------------------------------------------------------
# bread & continue
#-------------------------------------------------------------------------
# for i in range(10):
# 	if i==6:
# 		break
# 	if i==1 or i==3:
# 		continue
# 	print(i)




#-------------------------------------------------------------------------
# for x in dic
#-------------------------------------------------------------------------
# dic = {"a":1, "b":2, "c":3, "d":4}
# print(dic)
# for x in dic:
# 	print (x + ":" + str(dic[x]))



#-------------------------------------------------------------------------
# 多项赋值要这么写：
# first,rest = x[0], x[1:]
# 多项全局变量生命要这么写:
# global a,b,c
#-------------------------------------------------------------------------
# global a,b,c
# a,b,c = 1,2,3
# print("a:",a)
# print("b:",b)
# print("c:",c)






#-------------------------------------------------------------------------
# !!!可变长度参数	def foo(arg1,*tupleArg,**dictArg):
# 上面函数中的参数：
#	tupleArg前面“*”表示这个参数是一个元组参数，从程序的输出可以看出，默认值为()；
# 	dicrtArg前面有“**”表示这个字典参数(键值对参数)。
#	可以把tupleArg、dictArg看成两个默认参数。多余的非关键字参数，函数调用时被放在元组参数tupleArg中；
#	多余的关键字参数，函数调用时被放字典参数dictArg中
#-------------------------------------------------------------------------
# def foo(arg1,*tupleArg,**dictArg):
# 	print ("arg1=",arg1)  #formal_args
# 	print ("tupleArg=",tupleArg)  #()
# 	print ("dictArg=",dictArg)    #[]

# foo("formal_args")
# print(5*'*')
# foo(1,2,3,4,5,)
# print(5*'*')
# foo(5,6,7,8,a = 'ab', b = 'bc', c = 'cd', d = 'de')
# print("\n\n")



# 如果是函数定义中参数前的*表示的是将调用时的多个参数放入元组中,**则表示将调用函数时的关键字参数放入一个字典中
# def foo(arg1,arg2="OK",*tupleArg,**dictArg):
#     print ("arg1=",arg1)
#     print ("arg2=",arg2)
#     for i,element in enumerate(tupleArg):
#         print ("tupleArg %d-->%s" % (i,str(element)))
#     for  key in dictArg:
#         print ("dictArg %s-->%s" %(key,dictArg[key]))

# myList=["my1","my2"]
# myDict={"name":"Tom","age":22}
# foo("formal_args",arg2="argSecond",a=1)
# print ("*"*40)
# foo(123,myList,myDict)
# print ("*"*40)
# foo(123,rt=1234567890,*myList,**myDict)








#-------------------------------------------------------------------------
# !!!  xxx.vbs 执行CMD命令  createobject("wscript.shell").exec("calc")
#-------------------------------------------------------------------------
# print("在.vbs文件中,仅用下面一行命令即可执行cmd命令:")
# print('createobject("wscript.shell").exec("calc")')
# print("相较于.bat的好处是,没有弹框")






#-------------------------------------------------------------------------
# str.center()
#-------------------------------------------------------------------------
# switch = False
# print(30 * "_" + "switch:" + (not switch and "On" or "Off"))
# print(" exit ".center(80, '_'))






#-------------------------------------------------------------------------
# simple new thread!!!
# threading.Thread(target=fun, args=(arg1,)).start()
#-------------------------------------------------------------------------
# import threading
# from time import ctime,sleep

# def music(func):
#     for i in range(2):
#         print ("I was listening to %s. %s" %(func,ctime()))
#         sleep(1)

# def move(func):
#     for i in range(2):
#         print ("I was at the %s! %s" %(func,ctime()))
#         sleep(1)


# if __name__ == '__main__':
#     # music(u'爱情买卖')
#     # move(u'阿凡达')
#     threading.Thread(target=music, args=(u'爱情买卖',)).start()
#     threading.Thread(target=move, args=(u'阿凡达',)).start()

#     print ("end of story. %s" %ctime())




#-------------------------------------------------------------------------
# 实现了以前的一个想法:
# 唯一标识线程,可以用(线程名+时间).hash()
#-------------------------------------------------------------------------

# import threading

# def thread_main():
# 	name = threading.currentThread().getName()
# 	print(name)
# 	print(threading.currentThread().getName().__hash__())
# 	for x in range(10):
# 		print(x)

# threads = []
# for x in range(5):
# 	threads.append(threading.Thread(target=thread_main))
# for t in threads:
# 	t.start()




#-------------------------------------------------------------------------
# threading
#-------------------------------------------------------------------------
# import string, threading, time
# import threading

# def thread_main(a):
# 	global count, mutex
# 	# 获得线程名
# 	threadname = threading.currentThread().getName()

# 	for xx in range(0,10):
# 		print(xx)

# 	for x in range(0, int(a)):
# 	    # 取得锁
# 	    mutex.acquire()
# 	    count = count + 1
# 	    # 释放锁
# 	    mutex.release()
# 	    print (threadname, x, count)
# 	    time.sleep(1)
 
# def main(num):
# 	global count, mutex
# 	threads = []
 
# 	count = 1
# 	# 创建一个锁
# 	mutex = threading.Lock()
# 	# 先创建线程对象
# 	for x in range(0, num):
# 		threads.append(threading.Thread(target=thread_main, args=(10,)))
# 	# 启动所有线程
# 	for t in threads:
# 		t.start()
# 	# 主线程中等待所有子线程退出
# 	for t in threads:
# 		t.join() 
 
 
# if __name__ == '__main__':
# 	num = 4
# 	# 创建4个线程
# 	main(4)





#-------------------------------------------------------------------------
# print dir()
#-------------------------------------------------------------------------
# def g():
# 	yield 1

# i = g()
# print([s for s in dir(i) if not s.startswith('_')])






#-------------------------------------------------------------------------
# classic yield !!  "Generate all combinations of k elements from list x."
#-------------------------------------------------------------------------
# def gcomb(x,k):
# 	if k > len(x):
# 		return
# 	if k == 0:
# 		yield []
# 	else:
# 		first, rest = x[0], x[1:]
# 		for c in gcomb(rest, k-1):
# 			c.insert(0,first)
# 			yield c
# 		for c in gcomb(rest, k):
# 			yield c

# l = range(1,6)
# print(list(l))
# for c in gcomb(l`1, 2):
# 	print("", c)

# seq = range(1,5)
# for k in range(len(seq) + 2):
# 	print("%d-combs of %s" % (k, seq))
# 	for c in gcomb(seq, k):
# 		print(" ", c)


#-------------------------------------------------------------------------
# yield
# Ensure that explicitly raising StopIteration acts like any other exception
# in try/except, not like a return.
#-------------------------------------------------------------------------
# def g():
# 	yield 1
# 	try:
# 	    raise StopIteration
# 	except:
# 	    yield 2
# 	yield 3

# print (list(g()))



#-------------------------------------------------------------------------
# Guido's binary tree example.
#-------------------------------------------------------------------------
# class Tree:

# 	def __init__(self, label, left=None, right=None):
# 		self.label = label
# 		self.left = left
# 		self.right = right

# 	def __repr__(self, level=0, indent="	"):
# 		s = level*indent + repr(self.label)
# 		if self.left:
# 			s = s + "\\n" + self.left.__repr__(level+1, indent)
# 		if self.right:
# 			s = s + "\\n" + self.right.__repr__(level+1, indent)
# 		return s

# 	def __iter__(self):
# 		return inorder(self)

# def tree(list):
# 	n = len(list)
# 	if n == 0:
# 		return []
# 	i = n // 2
# 	return Tree(list[i], tree(list[:i]), tree(list[i+1:]))

# def inorder(t):
# 		if t:
# 			for x in inorder(t.left):
# 				yield x
# 			yield t.label
# 			for x in inorder(t.right):
# 				yield x

# t = tree("ABCDEFG")
# for x in inorder(t):
# 	print (x)

# print("t.label:", t.label)
# print("t.left:", t.left)
# print("t.right:", t.right)




#-------------------------------------------------------------------------
# yield generator:creator & caller
#-------------------------------------------------------------------------
# def yrange(n):
# 	for i in range(n):
# 		yield i

# def creator():
# 	r = yrange(5)
# 	print ("creator", r.__next__())
# 	return r

# def caller():
# 	r = creator()
# 	for i in r:
# 		print ('caller',i)

# caller()




#-------------------------------------------------------------------------
# yield
#-------------------------------------------------------------------------
# def h():
#     print ('Wen Chuan',)
#     m = yield 5  # Fighting!
#     print (m)
#     d = yield 12
#     print ('We are together!')
# c = h()
# m = c.__next__()  #m 获取了yield 5 的参数值 5
# d = c.send('Fighting!')  #d 获取了yield 12 的参数值12
# print ('We will never forget the date', m, '.', d)





#-------------------------------------------------------------------------
# ndict(zip(l1, l2))  用列表生成字典
#-------------------------------------------------------------------------
# l1 = [x for x in range(0,10)]
# l2 = [x*x for x in range(0,10)]

# z = zip(l1, li2)
# dic = dict(z)
# print (dic)




#-------------------------------------------------------------------------
# new thread
#-------------------------------------------------------------------------

# import time
# import _thread as thread

# def fun():
# 	print('This running in new threadself.')
	

# thread.start_new_thread(fun, ())
# time.sleep(1)


#-------------------------------------------------------------------------
# tkinter GUI  gui
#-------------------------------------------------------------------------
# from tkinter import *
# root = Tk()
# root.title("hello world")
# root.geometry('200x100')                 #是x 不是*
# root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True
# root.mainloop()



#-------------------------------------------------------------------------
# 没有global语句，是不可能为定义在函数外的变量赋值的
# global  全局变量的赋值
# 只读取全局变量，不需用global声明全局变量即可读取
# ！要赋值全局变量（修改全局变量的[指向]），则必须用global声明全局变量后才可赋值，--否则会赋值到新创建的与全局变量同名的本地变量上去
#-------------------------------------------------------------------------
# shortcuts = {}
# combine_keys_inclusion = []
# combine_record = {}

# def init():
# 	global shortcuts
# 	global combine_keys_inclusion
# 	ctrl_key = 'Lcontrol'
# 	alt_key = 'Lmenu'	# 只有按下Ctrl键的同时按Alt键,才能Hook到'Lmenu'的'key down'消息,单独按Alt键时,Hook到的是'Lmenu'的'key sys down'消息
# 	exit_key = 'Insert'		# 按下Shift键时，'Numpad0'键会变为'Insert'键
# 	switch_key = 'Numpad0'
# 	type_time_key = 'Numpad1'

# 	combine_keys_exit = (ctrl_key, alt_key, exit_key)
# 	combine_keys_switch = (ctrl_key, alt_key, switch_key)
# 	combine_keys_time_type = (type_time_key,)

# 	shortcuts = {	combine_keys_exit:1, 
# 					combine_keys_switch:2, 
# 					combine_keys_time_type:3}
# 	combin_keys_repeat = ()
# 	for shortcut in shortcuts.keys():
# 		combin_keys_repeat += shortcut
# 		print ("combin_keys_repeat:")
# 		print (combin_keys_repeat)
# 	combine_keys_inclusion = set(combin_keys_repeat)
# 	print ("set(combin_keys_repeat):")
# 	print (set(combin_keys_repeat))
# 	print ("combine_keys_inclusion:")
# 	print (combine_keys_inclusion)

# 	for key in combine_keys_inclusion:
# 		combine_record[key] = 0
# 		# combine_record = {'Numpad1': 0, 'Lmenu': 0, 'Insert': 0, 'Lcontrol': 0, 'Numpad0': 0}

# def fun():
# 	print (shortcuts)
# 	print (combine_keys_inclusion)
# 	print (combine_record)

# init()
# fun()




#-------------------------------------------------------------------------
# 表达式 三目运算  and or    if else   not
#-------------------------------------------------------------------------
# handler_switch = False
# handler_switch = not handler_switch
# print("on_switch:" + (handler_switch and "On" or "Off"))
# def func():
# 	global handler_switch
# 	handler_switch = not handler_switch
# 	print("on_switch:" + (handler_switch and "On" or "Off"))
# 	a = '123' if handler_switch else '456'
# 	a = (a + 'b' if handler_switch else a + 'c')
# 	print("___________ not return ___________" + a)
# func()
# func()
# func()



#-------------------------------------------------------------------------
# inspect.stack()[1][3]  获取当前XX名
#-------------------------------------------------------------------------
# import inspect

# def get_current_function_name():
#     return inspect.stack()[1][3]

# class MyClass:
#     def function_one(self):
#         print ("%s.%s invoked"%(self.__class__.__name__, get_current_function_name()))

# if __name__ == "__main__":
#     myclass = MyClass()
#     myclass.function_one()



#-------------------------------------------------------------------------
# __file__  获取当前文件名(包含路径)
# filename = __file__.split("\\")[-1]  文件名
#-------------------------------------------------------------------------
# print ('myname:',__file__)
# filename = __file__.split("\\")[-1]
# print (filename)




#-------------------------------------------------------------------------
# def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
# 对文件open第二参数默认'r' -- 不会自动创建文件
#-------------------------------------------------------------------------
# import time
# time_text = time.strftime("%Y-%m-%d",time.localtime(time.time()))
# programFileName = filename = __file__.split("\\")[-1]
# logFileName = r"F:\Log" + "\\" + programFileName + time_text + r".log"
# f = open(logFileName,'a')
# f.write(time_text + "\n")
# f.close()



# a = open(r'1234.log')
# a.close()



#-------------------------------------------------------------------------
# logging 模块的配置
#（日志级别默认为WARNING   等级 NOTSET < DEBUG < INFO < WARNING < ERROR < 等级CRITICAL）

# 以便记录日志到文件
# 配置追加模式打开文件,会自动创建文件 -- filemode='a'
#-------------------------------------------------------------------------
# import logging

# logging.basicConfig(level=logging.DEBUG,
#     format='%(levelname)s\t%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s\t%(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     # 配置日志文件路径
#     filename=r'F:\Log\123.log',
#     filemode='a')

# logging.debug("this is debug message")
# logging.info('This is info message')
# logging.warning('This is warning message')



#-------------------------------------------------------------------------
# try & except --This is not a useful wat...
#-------------------------------------------------------------------------
# import os

# def main():
# 	file_path = r'F:\Python\projects\hook\hook.py'
# 	file_input = open(file_path)
# 	file_input.close()

# if __name__ == "__main__":
# 	try:
# 		main()
# 	except Exception as e:
# 		print(e)
# 	pass




#-------------------------------------------------------------------------
# try & except
#-------------------------------------------------------------------------
# try:
#     import os
#     import commons
#     from execptions import FilePathException as FPE
# except Exception as e:
#     print(e)
# pass





#-------------------------------------------------------------------------
# '''1
# 2
# 3'''   是为了避免写\n    r'F:\Python\hook\hook.py' 是为了避免转义
#-------------------------------------------------------------------------
# a = '''1\n2
# 3''' 
# b = 'F:\nPython\projects\hook\hook.py'
# c = r'F:\nPython\projects\hook\hook.py'
# d = 'F:\\Python\\projects\\hook\\hook.py'

# print (a)
# print (b)
# print (c)
# print (d)


#-------------------------------------------------------------------------
# 	print ("str", int)
#-------------------------------------------------------------------------

# print("123",678,17051195617)





#-------------------------------------------------------------------------
# ** // % 乘方 整除 取余 List转换
#-------------------------------------------------------------------------
# print(2**3)
# print(5//2)
# print(9%2)
# a = (1,2,3)
# print(list(a))





#-------------------------------------------------------------------------
# strip('abc')
#-------------------------------------------------------------------------
# str = '	ab c' + 'd ef'
# str1 = str.strip()
# str2 = str1.strip('a')

# print (str[-3:])
# print (str)
# print(str1)
# print(str2)




#-------------------------------------------------------------------------
# pyhook
#-------------------------------------------------------------------------
# import pyHook
# import pythoncom

# def init():
# 	global LOG_DIR
# 	LOG_DIR = '''F:\Log'''


# def onMouseEvent(event):
# 	print ("MessageName:",event.MessageName)
# 	print ("Message:", event.Message)
# 	print ("Time:", event.Time)
# 	print ("Window:", event.Window)
# 	print ("WindowName:", event.WindowName)
# 	print ("Position:", event.Position)
# 	print ("Wheel:", event.Wheel)
# 	print ("Injected:", event.Injected)
# 	print ("---")
# 	return True

# def onKeyboardEvent(event):
# 	print ("MessageName:", event.MessageName)
# 	print ("Message:", event.Message)
# 	print ("Time:", event.Time)
# 	print ("Window:", event.Window)
# 	print ("WindowName:", event.WindowName)
# 	print ("Ascii:", event.Ascii, chr(event.Ascii))
# 	print ("Key:", event.Key)
# 	print ("KeyID:", event.KeyID)
# 	print ("ScanCode:", event.ScanCode)
# 	print ("Extended:", event.Extended)
# 	print ("Injected:", event.Injected)
# 	print ("Alt", event.Alt)
# 	print ("Transition", event.Transition)
# 	print ("---")
# 	return True

# def main():
# 	init()
# 	# 创建一个“钩子”管理对象
# 	hm = pyHook.HookManager()
# 	# 监听所有键盘事件
# 	hm.KeyDown = onKeyboardEvent
# 	# 设置键盘“钩子”
# 	hm.HookKeyboard()   
# 	# 监听所有鼠标事件
# 	# hm.MouseAll = onMouseEvent
# 	# 设置鼠标“钩子”
# 	# hm.HookMouse()
# 	# 进入循环，如不手动关闭，程序将一直处于监听状态
# 	pythoncom.PumpMessages()

# if __name__ == "__main__":   
# 	main()


#-------------------------------------------------------------------------
# addToClipBoard & cmd command
#-------------------------------------------------------------------------
# import os
# import time

# def addToClipBoard(text):
# 	command = 'echo ' + text.strip() + '| clip'
# 	os.system(command)

# time_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
# addToClipBoard(time_str)

# # read the clipboard
# from tkinter import Tk
# r = Tk()
# c = r.clipboard_get()
# print(c)





#-------------------------------------------------------------------------
# PrimeGenerator
#-------------------------------------------------------------------------
# import math

# class PrimeGenerator:

# 	def __init__(self):
# 		self.crossedOut = []
# 		self.result = []

# 	def generatePrimes(self, maxValue):
# 		if maxValue < 2:
# 			return []
# 		else:
# 			self.__uncrossIntegersUpTo(maxValue)
# 			self.__crossOutMultiples()
# 			self.__putUncrossedIntegersIntoResult()
# 			return self.result

# 	def __uncrossIntegersUpTo(self,maxValue):
# 		for i in range(2, maxValue + 1):
# 			self.crossedOut.append(False);

# 	def __crossOutMultiples(self):
# 		limit = int(math.sqrt(len(self.crossedOut)))
# 		for i in range(2, limit):
# 			if(self.__notCrossed(i)):
# 				self.__crossOutMultiplesOf(i)

# 	def __putUncrossedIntegersIntoResult(self):
# 		for i in range(2, len(self.crossedOut)):
# 			if self.__notCrossed(i):
# 				self.result.append(i)

# 	def __notCrossed(self,i):
# 		return self.crossedOut[i] == False

# 	def __crossOutMultiplesOf(self, i):
# 		for multiple in range(2*i, len(self.crossedOut), i):
# 			self.crossedOut[multiple] = True

# generator = PrimeGenerator()
# print (generator.generatePrimes(50))




#-------------------------------------------------------------------------
# double 转 int
#-------------------------------------------------------------------------
# d = 3.94
# print int(d)



#-------------------------------------------------------------------------
# 测试在获取urllib.urlopen后的网页中提取图片链接
#-------------------------------------------------------------------------
# import urllib
# import re

# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html

# def getImg(html):
#     reg = r'src="(.+?\.jpg)" pic_ext'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     x = 0
#     for imgurl in imglist:
#     	print imgurl
#         x+=1

# html = getHtml("http://tieba.baidu.com/p/3102805968")
# print getImg(html)




#-------------------------------------------------------------------------
# 测试urllib.urlopen.read()获取网页源码
#-------------------------------------------------------------------------
# import urllib

# # url = 'https://www.baidu.com/index.php?tn=monline_3_dg'
# url = 'http://tieba.baidu.com/p/3102805968'
 
# page = urllib.urlopen(url)
# # print type(page)
# # print dir(page)
# # print page.geturl()
# html = page.read()
# print html



#-------------------------------------------------------------------------
# 爬虫  使用urllib.urlretrieve()下载爬取到的网页图片
#-------------------------------------------------------------------------
# import urllib
# import re
 
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
 
# def getImg(html):
#     reg = r'src="(.+?\.jpg)" pic_ext'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     x = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'%s.jpg' % x)
#         x+=1
 
# html = getHtml("http://tieba.baidu.com/p/3102805968")
# print getImg(html)







#-------------------------------------------------------------------------
# 定义类 以创建类对象
#-------------------------------------------------------------------------
#类定义  
# class people:  
#     #定义基本属性  
#     name = ''  
#     age = 0  
#     #定义私有属性,私有属性在类外部无法直接进行访问  
#     __weight = 0  
#     #定义构造方法  
#     def __init__(self,n,a,w):  
#         self.name = n  
#         self.age = a  
#         self.__weight = w  
#     def speak(self):  
#         print("%s is speaking: I am %d years old" %(self.name,self.age))  
  
# p = people('tom',10,30)  
# p.speak()  









#-------------------------------------------------------------------------
# 测试 os.system('jar cvf 文件名.jar 路径/ 文件.后缀') 效果
#-------------------------------------------------------------------------
# import os
# # os.chdir(TE_SDK_PAGH)
# os.chdir(r"C:\Users\admin\Desktop\123")
# os.system('jar cvf ggg.jar .')










#-------------------------------------------------------------------------
# 测试 os.chdir(r'C:\Users\admin\Desktop\123') 
# 	以达到 'cd C:\Users\admin\Desktop\123'的效果
#-------------------------------------------------------------------------
# import os
# os.chdir(r'C:\Users\admin\Desktop\123')
# os.system('md 1234')







#-------------------------------------------------------------------------
# 测试 操作包含中文的路径名/文件名
#-------------------------------------------------------------------------
# import os
# print '中文'
# str = 'copy ' + 'C:\\Users\\gWX289620\\Desktop' + '\\自测用例.xlsm ' + 'C:\\Users\\gWX289620\\Desktop\\TE_package_01-14_16-56-10'
# os.system(str.decode('utf8').encode('gbk'))
# shutil.copyfile(DOC_PATH4.decode('utf8').encode('gbk'), (OUTPATH + "自测用例.xlsm").decode('utf8').encode('gbk'))






#-------------------------------------------------------------------------
# 测试 import shutil
#-------------------------------------------------------------------------
# import shutil








#-------------------------------------------------------------------------
# 测试 os.path.exists()
#-------------------------------------------------------------------------
# import os
# TE_DEMO_PATH = "D:\Android\eclipse-adt\workspace\TEDemo"
# print os.path.exists(TE_DEMO_PATH)







#-------------------------------------------------------------------------
# 测试 help(os)
#-------------------------------------------------------------------------
# import os
# print dir(os)
# print help(os)








#-------------------------------------------------------------------------
# 测试 git push --set-upstream origin master 后能否直接 git push
#-------------------------------------------------------------------------
# 结果是可以的，远程git仓库的内容有更新
# $ git push
# warning: push.default is unset; its implicit value has changed in
# Git 2.0 from 'matching' to 'simple'. To squelch this message
# and maintain the traditional behavior, use:

#   git config --global push.default matching

# To squelch this message and adopt the new behavior now, use:

#   git config --global push.default simple

# When push.default is set to 'matching', git will push local branches
# to the remote branches that already exist with the same name.

# Since Git 2.0, Git defaults to the more conservative 'simple'
# behavior, which only pushes the current branch to the corresponding
# remote branch that 'git pull' uses to update the current branch.

# See 'git help config' and search for 'push.default' for further information.
# (the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
# 'current' instead of 'simple' if you sometimes use older versions of Git)

# Counting objects: 3, done.
# Delta compression using up to 4 threads.
# Compressing objects: 100% (3/3), done.
# Writing objects: 100% (3/3), 402 bytes | 0 bytes/s, done.
# Total 3 (delta 2), reused 0 (delta 0)
# To git@github.com:gbwgithub/g-py.git
#    0f26825..66cd4a7  master -> master









#-------------------------------------------------------------------------
# 测试 Ctrl + Shift + L可以将当前选中区域打散，然后进行同时编辑，
# 有打散自然就有合并，Ctrl + J可以把当前选中区域合并为一行
#-------------------------------------------------------------------------
# values = ['awer', 'b', 'c', 'd', 'e ', 'f ', 'g']










#-------------------------------------------------------------------------
# 测试代码提示 -- SublimeCodeIntel
#-------------------------------------------------------------------------
# a = '123123123123'
# print a.endswith('\n')












#-------------------------------------------------------------------------
# 测试字符串长度，去掉行尾'\n'
#-------------------------------------------------------------------------
# a = '123\n'
# print len(a)
# b = a[0:len(a)-1]
# print b
# print len(b)













#-------------------------------------------------------------------------
# 测试打开一个文本文件，如何在文件尾加入一个空行
#-------------------------------------------------------------------------
# f = open(r'C:\Users\gWX289620\Desktop\123.txt')
# lines = f.readlines()
# f.close()
# i = 0
# for line in lines:
# 	i += 1
# 	print str(i) + ":"
# 	print line
# 	if '\n' in line:
# 		print "yes"
# 	else:
# 		print "no"	














#-------------------------------------------------------------------------
# 测试如何判断一个变量是否定义
#-------------------------------------------------------------------------
# print dir()

# assert not 'awer' in dir()

# if 'awer' in dir():
# 	print 'awer is def'
# else:
# 	print 'awer is not def'

# awer = ''

# if 'awer' in dir():
# 	print 'awer is def'
# else:
# 	print 'awer is not def'

# print dir()
