#coding=utf-8

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
# 测试获取urllib.urlopen后的网页链接
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
#     	# print imgurl
#         x+=1

# html = getHtml("http://tieba.baidu.com/p/3102805968")
# print getImg(html)




#-------------------------------------------------------------------------
# 测试urllib.urlopen
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
# 爬虫 爬取网页图片
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
# getImg(html)





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
