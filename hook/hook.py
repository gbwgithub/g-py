#coding=utf-8
#!/usr/bin/env python
# 启动 pythonw2 F:\Python\projects\hook\hook.py


# 消息Hook随开机启动常驻，退出按键胜场两个shortcut 半退出开关只是控制是否记录日志，以及是否开启功能键
# 添加功能键，结束所有非Hook.py的python进程
# 写一个启动程序，一个测试程序，分开

import pyHook
import pythoncom
import sys
sys.path.append(r'F:\Python\projects\hook')
import hook_handler

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
	global shortcuts, combine_keys_inclusion, combine_record

	type_time_key = 'Numpad1'
	type_html_key = 'Numpad2'

	ctrl_key = 'Lcontrol'
	alt_key = 'Lmenu'	# 只有按下Ctrl键的同时按Alt键,才能Hook到'Lmenu'的'key down'消息,单独按Alt键时,Hook到的是'Lmenu'的'key sys down'消息
	exit_key = 'Insert'		# 按下Shift键时，'Numpad0'键会变为'Insert'键
	switch_key = 'Numpad0'

	combine_keys_time_type = (type_time_key,)
	combine_keys_html_type = (type_html_key,)
	combine_keys_exit = (ctrl_key, alt_key, exit_key)
	combine_keys_switch = (ctrl_key, alt_key, switch_key)

	shortcuts = {	combine_keys_exit:hook_handler.on_exit, 
					combine_keys_switch:hook_handler.on_switch, 
					combine_keys_time_type:hook_handler.on_type_time,
					combine_keys_html_type:hook_handler.on_type_html}
	combin_keys_repeat = []
	for shortcut in shortcuts.keys():
		combin_keys_repeat += shortcut
	combine_keys_inclusion = set(combin_keys_repeat)

	combine_record = {}
	for key in combine_keys_inclusion:
		combine_record[key] = 0

def on_key_down(event):
	hook_handler.__on_key_down(event)
	return __check_key_event(event)

def on_key_up(event):
	hook_handler.__on_key_up(event)
	return __check_key_event(event)

def __check_key_event(event):
	if(event.Key in combine_keys_inclusion):
		return __on_combine_keys(event)
	return True

def __on_combine_keys(event):
	if('key up' == event.MessageName):
		combine_record[event.Key] = 0
		return True
	elif('key down' == event.MessageName):
		combine_record[event.Key] = 1
		return __check_shortcuts_down()
	else:
		return True

def __check_shortcuts_down():
	for shortcut in shortcuts.keys():
		if(__check_shortcut_down(shortcut)):
			return shortcuts[shortcut]()		# 执行快捷键操作
	return True

def __check_shortcut_down(shortcut):
	for key in shortcut:
		if(0 == combine_record[key]):
			return False
	return True

if __name__ == "__main__":


	main()