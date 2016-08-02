#coding=utf-8
#!/usr/bin/env python

#TODO 响应快捷键,调用其他函数复制时间，上传到GITHUB

import pyHook
import pythoncom
import time
import os
import sys
import logging
import fileutil

def main():
	# 初始化
	init()
	# 创建一个“钩子”管理对象
	hm = pyHook.HookManager()
	# 监听所有键盘事件
	hm.KeyDown = on_key_down
	hm.KeyUp = on_key_up
	# 设置键盘“钩子”
	hm.HookKeyboard()
	# 进入循环，如不手动关闭，程序将一直处于监听状态
	pythoncom.PumpMessages()

def init():
	global EXIT_KEY
	global TIME_COPY_KEY
	global CTRL_KEY
	global ALT_KEY
	global COMBINE_KEYS_EXIT
	global COMBINE_KEYS
	global SHORTCUTS
	global LOG_DIR
	global LOG_FILE
	CTRL_KEY = 'Lcontrol'
	ALT_KEY = 'Lmenu'	#只有按下Ctrl键的同时按Alt键,才能Hook到'Lmenu'的'key down'消息,单独按Alt键时,Hook到的是'Lmenu'的'key sys down'消息
	LOG_DIR = r'F:\Log'
	LOG_FILE = LOG_DIR + r'\keyboard_hook.log'

	EXIT_KEY = 'Numpad0'
	COMBINE_KEYS_EXIT = (CTRL_KEY, ALT_KEY, EXIT_KEY)
	TIME_COPY_KEY = 'Numpad1'
	COMBINE_KEYS_TIME_COPY = (CTRL_KEY, ALT_KEY, TIME_COPY_KEY)

	SHORTCUTS = {COMBINE_KEYS_EXIT:on_exit, COMBINE_KEYS_TIME_COPY:on_time_to_clipboard}
	combin_keys_all = ()
	for shortcut in SHORTCUTS:
		combin_keys_all += shortcut
	COMBINE_KEYS = set(combin_keys_all)

	global combine_record
	combine_record = {}
	for key in COMBINE_KEYS:
		combine_record[key] = 0

	fileutil.mkdir(LOG_DIR)
	logging.basicConfig(level=logging.DEBUG,
	                    format='%(asctime)s\t%(levelname)s %(filename)s %(funcName)s [line:%(lineno)d]\t%(message)s',
	                    datefmt='%Y-%m-%d %H:%M:%S',
	                    filename=LOG_FILE,		# 配置日志文件路径
	                    filemode='a')

def on_exit():
	logging.info("_________________________________ exit _________________________________")
	sys.exit()
	pass

def on_time_to_clipboard():
	time_text = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	command = 'echo ' + time_text.strip() + '| clip'
	os.system(command)
	logging.info("copytime:" + time_text)
	pass

def on_key_down(event):
	logging.debug("WindowName:" + event.WindowName)
	logging.debug("MessageName:" + event.MessageName)
	logging.debug("Key:" + event.Key)
	logging.debug("---")
	__check_key_event(event)
	return True

def on_key_up(event):
	logging.debug("MessageName:" + event.MessageName)
	logging.debug("Key:" + event.Key)
	logging.debug("---")
	__check_key_event(event)
	return True

def __check_key_event(event):
	global COMBINE_KEYS
	if(event.Key in COMBINE_KEYS):
		__on_combine_keys(event)

def __on_combine_keys(event):
	global combine_record
	if('key up' == event.MessageName):
		combine_record[event.Key] = 0
	elif('key down' == event.MessageName):
		combine_record[event.Key] = 1
		__check_shortcuts_record()

def __check_shortcuts_record():
	global SHORTCUTS
	for shortcut in SHORTCUTS.keys():
		if(__check_shortcut(shortcut)):
			SHORTCUTS[shortcut]()		# 执行快捷键操作

def __check_shortcut(shortcut):
	global combine_record
	for key in shortcut:
		if(0 == combine_record[key]):
			return False
	return True

if __name__ == "__main__":   
	main()