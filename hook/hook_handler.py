#coding=utf-8
#!/usr/bin/env python

import time
import thread
import logging
from pykeyboard import PyKeyboard
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

def __on_key_down(event):
	if not log_switch:
		return True
	logging.debug("WindowName:" + event.WindowName if event.WindowName else "None")
	logging.debug("MessageName:" + event.MessageName)
	logging.debug("Key:" + event.Key)
	logging.debug("---")

def __on_key_up(event):
	if not log_switch:
		return True
	logging.debug("WindowName:" + event.WindowName if event.WindowName else "None")
	logging.debug("MessageName:" + event.MessageName)
	logging.debug("Key:" + event.Key)
	logging.debug("---")


def on_reset():
	logging.info(" reset ".center(80, '_'))
	command = 'F:\Python\projects\hook\hook_launch.vbs'
	os.system(command)
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
	PyKeyboard().type_string(time_text)
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
	html_text = 'not support html_text'
 	logging.info("on_type_html()")
	PyKeyboard().type_string(html_text)
	# command = 'echo ' + html_text.strip() + '| clip'
	# os.system(command)
	on_switch()
	return False		#返回False 以拦截

def on_End_analog():
	logging.info(30*'_' + " on_End_analog")
	k = PyKeyboard()
	#抬起功能按键Ctrl,否则End效果会变为Ctrl+End效果
	k.release_key(k.control_key)
	k.tap_key(k.end_key)
	return False

def on_End_combo():
	logging.info(30*'_' + " on_End_combo")
	k = PyKeyboard()
	#抬起功能按键Ctrl,否则End效果会变为Ctrl+End效果
	k.release_key(k.control_key)
	k.press_keys([k.end_key, ';', k.enter_key])
	return False

init()