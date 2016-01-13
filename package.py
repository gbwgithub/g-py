#coding=utf-8

import os
import sys
import time
import shutil
import zipfile
import glob
import fileutil

# 删除短时间内生成的TE_package文件夹，方便测试
def clear():
	# shutil.rmtree(OUTPATH)
	return

def init():
	global TE_DEMO_PATH
	global TE_SDK_PAGH
	global RUNTIME
	global OUTPATH

	TE_DEMO_PATH = r"D:\Android\eclipse-adt\workspace\TEDemo"
	TE_SDK_PAGH = r"D:\Android\eclipse-adt\workspace\TESDK"
	RUNTIME = time.strftime('%m-%d_%H-%M-%S',time.localtime(time.time()))
	OUTPATH = r'C:\Users\gWX289620\Desktop' + '\\' + 'TE_package_' + RUNTIME + '\\'

	print 'TEDemo	->	' + TE_DEMO_PATH if os.path.exists(TE_DEMO_PATH) else exit()
	print 'TESDK	->	' + TE_SDK_PAGH if os.path.exists(TE_SDK_PAGH) else exit()
	print 'outpath	->	' + OUTPATH


# 去掉TEDemo依赖项目TESDK的设置
def undepend():
	global properties_file
	global properties_lines
	global gradle_file
	global gradle_lines

	# # 去掉project.properties中的设置
	properties_file = TE_DEMO_PATH + '\\project.properties'
	properties_item	= 'android.library.reference'
	properties_lines = fileutil.remove_file_item(properties_file, properties_item)
	# # 去掉build.gradle中的设置
	gradle_file = TE_DEMO_PATH + '\\build.gradle'
	gradle_item = 'compile project'
	gradle_lines = fileutil.remove_file_item(gradle_file, gradle_item)

# 复制&压缩相关项目文件，复制时去掉TEDemo中不需要压缩的目录
def package():
	ignore_these = ['.git', '.svn', '.idea', '.settings', 'bin','build',
	'gen', 'libs/*', 'local.properties', 'projuard-project.txt', 'TEDemo.iml']
	def ignore_most(folder, files):
	    return ignore_these
	fileutil.mkdir(OUTPATH)
	# # 拷贝TEDemo工程
	shutil.copytree(TE_DEMO_PATH, OUTPATH + "TEDemo", False, ignore_most)
	# # 拷贝libs目录
	shutil.copytree(TE_SDK_PAGH + "\\libs", OUTPATH + "eSDK_TP_TEMobile_1.5.50_Android")
	# # 拷贝接口文档、开发指南、自测用例、转测excel
	# shutil.copyfile(DOC_PATH4, OUTPATH + "自测用例.xlsm") 这个功能不支持中文文件名，暂时不添加
	# 下次尝试调用cmd命令复制文件，来实现此功能
	# # 压缩TEDemo
	fileutil.zip(OUTPATH + "TEDemo", OUTPATH + "eSDK_TP_TEMobile_Demo_1.5.50_Android")
	# # 考虑使用java原生的命令打.jar包


# 还原TEDemo依赖项目TESDK的设置
def redepend():
	fileutil.restore_file(properties_file, properties_lines)
	fileutil.restore_file(gradle_file, gradle_lines)


# 运行.apk，进行测试
def test():
	# os.system('adb install ***.apk')
	# os.system('adb shell')
	# os.system('am start -n com.huawei.te.example/com.huawei.te.example.activity.LoginActivity')
	return

if __name__ == '__main__':
	print '-------------------- Start ---------------------'
	clear()
	init()
	undepend()
	package()
	redepend()
	test()
	print '-------------------- Finish --------------------'

