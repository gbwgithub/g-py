#coding=utf-8

import os
import zipfile

def mkdir(path):
 # 去除首位空格
 path=path.strip()
 # 去除尾部 \ 符号
 path=path.rstrip("\\")
 
 # 判断路径是否存在
 isExists=os.path.exists(path)

 # 判断结果
 if not isExists:
  # 如果不存在则创建目录
  os.makedirs(path)
  # print path + ' makedirs success.'
  return True
 else:
  # 如果目录存在则不创建，并提示目录已存在
  # print path + ' already exits.'
  return False
 
 
# 没用上
def replaceConfig(filename, item, content):
 input = open(filename)
 lines = input.readlines()
 input.close()
 
 output = open(filename, "w")
 for line in lines:
  if not line:
   break
  if line.startswith(item):
   temp = item + content
   output.write(line)
  else:
   ouput.write(line)
 
 output.close()


# 为文本文件最后加入一行空行
# TODO 这个函数不健壮
def emptyLastLine(filename):
 input = open(filename)
 lines = input.readlines()
 input.close()
 
 output = open(filename, "w")
 for line in lines:
  if not line:
    break
  if line.endswith('\n'):
    ouput.write(line)
  else:
    output.write(line)
    output.write('\n')
 
 output.close()
 

# 移除包含item的行，函数返回原来的文件内容
def remove_file_item(file, item):
 input = open(file)
 lines = input.readlines()
 input.close()
 output = open(file, "w")
 for line in lines:
  if not line:
   break
  if item in line:
   # 包含指定内容的行不写入文件
   print 'remove \"' + line[0:len(line)-1] + '\"  for a very short time.'
  else:
   output.write(line)
 output.close()

 return lines


# 以removeFileItem()的返回为参数，还原文件内容
def restore_file(file, lines):
  output = open(file, "w")
  for line in lines:
    if not line:
      break
    output.write(line)
  output.close()


# 压缩文件
def zip(src, dst):
  zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
  abs_src = os.path.abspath(src)
  for dirname, subdirs, files in os.walk(src):
    # zf.write(dirname)
    absname = os.path.abspath(dirname)
    arcname = absname[len(abs_src) + 1:]
    zf.write(os.path.abspath(dirname), arcname)
    for filename in files:
      absname = os.path.abspath(os.path.join(dirname, filename))
      arcname = absname[len(abs_src) + 1:]
      # print 'zipping %s as %s' % (os.path.join(dirname, filename), arcname)
      zf.write(absname, arcname)
  zf.close()