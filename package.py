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
	global USEING_ECLIPSE
	USEING_ECLIPSE = False

	global TE_DEMO_PATH
	global TE_SDK_PAGH
	global TE_SDK_BIN_PATH
	global TE_SDK_PACKAGE_NAME
	global TE_DEMO_PACKAGE_NAME
	global RUNTIME
	global OUTDIR
	global OUTPATH
	global PACKAGE_PATH
	global DOC1_PATH, DOC1_TO, DOC_NAME1
	global DOC2_PATH, DOC2_TO, DOC_NAME2
	global DOC3_PATH, DOC3_TO, DOC_NAME3
	global DOC4_PATH, DOC4_TO, DOC_NAME4

	# TE_DEMO_PATH = r"D:\Android\eclipse-adt\workspace\TEDemo"
	# TE_SDK_PAGH = r"D:\Android\eclipse-adt\workspace\TESDK"
	TE_DEMO_PATH = r"D:\Android\TEWorkspace\TEDemo"
	TE_SDK_PAGH = r"D:\Android\TEWorkspace\TESDK"
	if USEING_ECLIPSE:
		TE_SDK_BIN_PATH = TE_SDK_PAGH + r"\bin\classes"
	else:
		TE_SDK_BIN_PATH = TE_SDK_PAGH + r"\build\intermediates\classes\release"

	TE_SDK_PACKAGE_NAME = 'eSDK_TP_TEMobile_1.5.50_Android'
	TE_DEMO_PACKAGE_NAME = 'eSDK_TP_TEMobile_Demo_1.5.50_Android'
	OUTDIR = r'C:\Users\gWX289620\Desktop'
	RUNTIME = time.strftime('%m-%d_%H-%M-%S',time.localtime(time.time()))
	OUTPATH = OUTDIR + '\\' + 'TE_package_' + RUNTIME + '\\'
	PACKAGE_PATH = OUTPATH + 'package\\'

	DOC_NAME1 = 'eSDK TE Mobile V100R005C50 接口参考new (Android).doc'
	DOC_NAME2 = 'TE Android 登录语音视频呼叫开发指南.docx'
	DOC_NAME3 = 'eSDK_TE_Android_V100R005C50版本转测试.xls'
	DOC_NAME4 = '自测用例.xlsm'

	# 初始化文档文件路径
	DOC1_PATH = (OUTDIR + '\\' + DOC_NAME1)
	DOC2_PATH = (OUTDIR + '\\' + DOC_NAME2)
	DOC3_PATH = (OUTDIR + '\\' + DOC_NAME3)
	DOC4_PATH = (OUTDIR + '\\' + DOC_NAME4)
	DOC1_TO = PACKAGE_PATH + DOC_NAME1
	DOC2_TO = PACKAGE_PATH + DOC_NAME2
	DOC3_TO = PACKAGE_PATH + DOC_NAME3
	DOC4_TO = PACKAGE_PATH + DOC_NAME4

	print 'TEDemo	->	' + TE_DEMO_PATH if os.path.exists(TE_DEMO_PATH) else exit()
	print 'TESDK	->	' + TE_SDK_PAGH if os.path.exists(TE_SDK_PAGH) else exit()
	print 'TESDK bin	->	' + TE_SDK_BIN_PATH if os.path.exists(TE_SDK_BIN_PATH) else exit()
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

	# # TEDemo 去掉 project.properties中的设置
	properties_file = TE_DEMO_PATH + '\\project.properties'
	properties_item	= 'android.library.reference'
	properties_lines = fileutil.remove_file_item(properties_file, properties_item)
	# # TEDemo 去掉build.gradle中的设置
	gradle_file = TE_DEMO_PATH + '\\build.gradle'
	gradle_item = 'compile project'
	gradle_lines = fileutil.remove_file_item(gradle_file, gradle_item)

	# # TESDK 去掉 build.gradle中的 dependencies{}


def jar():
	fileutil.mkdir(OUTPATH)
	fileutil.mkdir(PACKAGE_PATH)
	# 拷贝TESDK bin 到 OUTPATH
	ignore_these = ['BuildConfig.class', 'R$attr.class', 'R$drawable.class', 'R$string.class', 'R.class']
	def ignore_most(folder, files):
	    return ignore_these
	shutil.copytree(TE_SDK_BIN_PATH, OUTPATH + "bin", False, ignore_most)

	# # 考虑使用java原生的命令打.jar包
	# jar 命令打包的文件，加压其中包含META-INF
	#	对照eclipse打包的jar文件，看是否也包含
	os.chdir(OUTPATH)
	os.system('jar cf TEMobile.jar -C ' + TE_SDK_PAGH + ' res/values -C ' + OUTPATH + 'bin .')


# 复制&压缩相关项目文件，复制时去掉了TEDemo中不需要压缩的目录
def package():
	ignore_these = ['.git', '.svn', '.idea', '.settings', 'bin','build',
	'gen', 'gradle' , 'libs/*', 'local.properties', 'projuard-project.txt', 'TEDemo.iml']
	def ignore_most(folder, files):
	    return ignore_these
	# # 拷贝TEDemo工程
	shutil.copytree(TE_DEMO_PATH, OUTPATH + TE_DEMO_PACKAGE_NAME, False, ignore_most)
	# # 拷贝libs目录
	shutil.copytree(TE_SDK_PAGH + "\\libs", OUTPATH + TE_SDK_PACKAGE_NAME)
	# # 拷贝生成的TEMobile.jar
	shutil.copyfile(OUTPATH + "TEMobile.jar", OUTPATH + TE_SDK_PACKAGE_NAME + "\\TEMobile.jar")
	# # 拷贝接口文档、开发指南、自测用例、转测excel
	shutil.copyfile(DOC1_PATH.decode('utf8').encode('gbk'), DOC1_TO.decode('utf8').encode('gbk'))
	shutil.copyfile(DOC2_PATH.decode('utf8').encode('gbk'), DOC2_TO.decode('utf8').encode('gbk'))
	shutil.copyfile(DOC3_PATH.decode('utf8').encode('gbk'), DOC3_TO.decode('utf8').encode('gbk'))
	shutil.copyfile(DOC4_PATH.decode('utf8').encode('gbk'), DOC4_TO.decode('utf8').encode('gbk'))

	# # 压缩TEDemo
	fileutil.zip(OUTPATH + TE_DEMO_PACKAGE_NAME, PACKAGE_PATH + TE_DEMO_PACKAGE_NAME)
	# # 压缩TESDK
	fileutil.zip(OUTPATH + TE_SDK_PACKAGE_NAME, PACKAGE_PATH + TE_SDK_PACKAGE_NAME)


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
	jar()
	package()
	redepend()
	test()
	print '-------------------- Finish --------------------'


if __name__ == '__main__':
	main()