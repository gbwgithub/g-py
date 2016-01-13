#coding=utf-8

import os
import sys
import time
import fileutil

print '-------------------- BEGIN ---------------------'

TE_DEMO_PATH = "D:\Android\eclipse-adt\workspace\TEDemo"
TE_SDK_PAGH = "D:\Android\eclipse-adt\workspace\TESDK"
RUNTIME = time.strftime('%m-%d %H-%M-%S',time.localtime(time.time()))
OUTPATH = r'C:\Users\gWX289620\Desktop' + '\\' + 'package ' + RUNTIME + '\\'

print 'runtime	->	' + RUNTIME
print 'TEDemo	->	' + TE_DEMO_PATH
print 'TESDK	->	' + TE_SDK_PAGH
print 'outpath	->	' + OUTPATH

# 去掉TEDemo依赖项目TESDK的设置
# # project.properties
properties_file = TE_DEMO_PATH + '\\project.properties'
properties_item	= 'android.library.reference'
properties_lines = fileutil.removeFileItem(properties_file, properties_item)
# # build.gradle
gradle_file = TE_DEMO_PATH + '\\build.gradle'
gradle_item = 'compile project'
gradle_lines = fileutil.removeFileItem(gradle_file, gradle_item)


# 复制一份项目文件，去掉TEDemo中 不需要压缩的目录 (.git与读取.gitignore中的内容）


# 还原TEDemo依赖项目TESDK的设置
fileutil.restoreFile(properties_file, properties_lines)
fileutil.restoreFile(gradle_file, gradle_lines)



# os.system('adb install ***.apk')
# os.system('adb shell')
# os.system('am start -n com.huawei.te.example/com.huawei.te.example.activity.LoginActivity')

# fileutil.mkdir(OUTPATH)
print '-------------------- END --------------------'