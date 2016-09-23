#coding=utf-8
#!/usr/bin/env python

import time
import thread
import logging
import pykeyboard
import os
import sys
sys.path.append("F:\Python\projects\g-utils")
import fileutil

log_switch = False
handler_switch = False

def init():
	log_dir = r'F:\Log'
	log_file = log_dir + r'\keyboard_hook.log'

	fileutil.mkdir(log_dir)
	logging.basicConfig(level=logging.DEBUG,
	                    format='%(asctime)s\t%(levelname)s %(filename)s %(funcName)s [line:%(lineno)d]\t%(message)s',
	                    datefmt='%Y-%m-%d %H:%M:%S',
	                    filename=log_file,		# 配置日志文件路径
	                    filemode='w')
	logging.info(" start ".center(80, '_'))

def on_exit():
	logging.info(" exit ".center(80, '_'))
	sys.exit()

def on_switch():
	global handler_switch
	handler_switch = not handler_switch
	logging.info(30 * "_" + "switch:" + (handler_switch and "On" or "Off"))
	return True

def on_type_time():
	if not handler_switch:
		return True
	time_text = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	logging.info("type_time:" + time_text)
	pykeyboard.PyKeyboard().type_string(time_text)
	on_switch()
	return False		#返回False 以拦截

def on_type_html():
	if not handler_switch:
		return True
	html_text = r'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
	<title></title>
</head>
<body>



</body>
</html>
'''
	logging.info("on_type_html()")
	pykeyboard.PyKeyboard().type_string(html_text)
	# command = 'echo ' + html_text.strip() + '| clip'
	# os.system(command)
	on_switch()
	return False		#返回False 以拦截

def __on_key_down(event):
	if not log_switch:
		return True
	logging.debug("WindowName:" + event.WindowName)
	logging.debug("MessageName:" + event.MessageName)
	logging.debug("Key:" + event.Key)
	logging.debug("---")

def __on_key_up(event):
	if not log_switch:
		return True
	logging.debug("WindowName:" + event.WindowName)
	logging.debug("MessageName:" + event.MessageName)
	logging.debug("Key:" + event.Key)
	logging.debug("---")

init()