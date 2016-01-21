#coding=utf-8

import os
import sys
import time
import shutil
import zipfile
import glob
import fileutil
import glob


def init():
	global TE_DEMO_PATH
	global TE_SDK_PAGH
	global RUNTIME
	global OUTDIR
	global OUTPATH
	global DOC1_PATH, DOC1_TO, DOC_NAME1
	global DOC2_PATH, DOC2_TO, DOC_NAME2
	global DOC3_PATH, DOC3_TO, DOC_NAME3
	global DOC4_PATH, DOC4_TO, DOC_NAME4

	TE_DEMO_PATH = r"D:\Android\eclipse-adt\workspace\TEDemo"
	TE_SDK_PAGH = r"D:\Android\eclipse-adt\workspace\TESDK"
	OUTDIR = r'C:\Users\gWX289620\Desktop'
	RUNTIME = time.strftime('%m-%d_%H-%M-%S',time.localtime(time.time()))
	OUTPATH = OUTDIR + '\\' + 'TE_package_' + RUNTIME + '\\'

	DOC_NAME1 = 'eSDK TE Mobile(Android) 接口参考.docx'
	DOC_NAME2 = 'TE Android 登录语音视频呼叫开发指南.docx'
	DOC_NAME3 = 'eSDK_TE_Android_V100R005C50版本转测试.xls'
	DOC_NAME4 = '自测用例.xlsm'

	# 初始化文档文件路径
	DOC1_PATH = (OUTDIR + '\\' + DOC_NAME1)
	DOC2_PATH = (OUTDIR + '\\' + DOC_NAME2)
	DOC3_PATH = (OUTDIR + '\\' + DOC_NAME3)
	DOC4_PATH = (OUTDIR + '\\' + DOC_NAME4)
	DOC1_TO = OUTPATH + DOC_NAME1
	DOC2_TO = OUTPATH + DOC_NAME2
	DOC3_TO = OUTPATH + DOC_NAME3
	DOC4_TO = OUTPATH + DOC_NAME4

	print 'TEDemo	->	' + TE_DEMO_PATH if os.path.exists(TE_DEMO_PATH) else exit()
	print 'TESDK	->	' + TE_SDK_PAGH if os.path.exists(TE_SDK_PAGH) else exit()
	print 'DOC1_PATH	->	' + DOC1_PATH if os.path.exists(DOC1_PATH.decode('utf8').encode('gbk')) else exit()
	print 'DOC2_PATH	->	' + DOC2_PATH if os.path.exists(DOC2_PATH.decode('utf8').encode('gbk')) else exit()
	print 'DOC3_PATH	->	' + DOC3_PATH if os.path.exists(DOC3_PATH.decode('utf8').encode('gbk')) else exit()
	print 'DOC4_PATH	->	' + DOC4_PATH if os.path.exists(DOC4_PATH.decode('utf8').encode('gbk')) else exit()
	print 'outpath	->	' + OUTPATH


# 删除短时间内生成的TE_package文件夹，方便测试
def clear():
	# shutil.rmtree(OUTPATH)
	for dir_package in glob.glob(OUTDIR + '\\' + 'TE_package_*'):
		print 'rmtree -> ' + dir_package
		shutil.rmtree(dir_package)


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


def jar():
	# # 考虑使用java原生的命令打.jar包
	# jar 命令打包的文件，加压其中包含META-INF
	#	对照eclipse打包的jar文件，看是否也包含
	os.chdir(TE_SDK_PAGH)
	# os.system('jar cvf 文件名.jar 路径/ 文件.后缀')
	print 'jar() is TODO...'


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
	shutil.copyfile(DOC1_PATH.decode('utf8').encode('gbk'), DOC1_TO.decode('utf8').encode('gbk'))
	shutil.copyfile(DOC2_PATH.decode('utf8').encode('gbk'), DOC2_TO.decode('utf8').encode('gbk'))
	shutil.copyfile(DOC3_PATH.decode('utf8').encode('gbk'), DOC3_TO.decode('utf8').encode('gbk'))
	shutil.copyfile(DOC4_PATH.decode('utf8').encode('gbk'), DOC4_TO.decode('utf8').encode('gbk'))

	# # 压缩TEDemo
	fileutil.zip(OUTPATH + "TEDemo", OUTPATH + "eSDK_TP_TEMobile_Demo_1.5.50_Android")


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


def main():
	print '-------------------- Start ---------------------'
	init()
	clear()
	undepend()
	package()
	redepend()
	test()
	print '-------------------- Finish --------------------'


if __name__ == '__main__':
	main()