#coding=utf-8
#!/usr/bin/env python
import os

def main():
	test_hook()

def test_hook():
	hook_path = r'F:\Python\projects\hook\hook.py'
	command = 'python2 ' + hook_path
	print(command)
	os.system(command)

if __name__ == "__main__":
	main()