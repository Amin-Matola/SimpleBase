import os
import time
from jsonifier import *



def runner(command):
	func	= compile(command,'test','eval')
	try:
		exec(func)
	except Exception as e:
		print(" Command ",command," not recognized!")
	print('')
	get()


os.system("cls")
print(" Simple Base Version 0.1.0, Initial Release On %s (Version %s.%s.%s)."%(os.sys.platform,
	os.sys.getwindowsversion().platform_version[0],
	os.sys.getwindowsversion().platform_version[1],
	os.sys.getwindowsversion().platform_version[2]))
print(" "+time.ctime(),"(%s)"%time.tzname[0])
print("*"*75+"\n")

def get():

	line=input(":sb> ")
	if not line:
		get()
	if(line=='quit'):
		return None
	if len(line.split(' '))>1:
		words=line.split(' ')
		if not len(line.split('('))>1:
			if len(words)>=3:
				value=words.pop()
				if len(value.split(','))>1:
					line="_".join(words)+"('%s',"%value.split(',')[0]
					for a in value.split(',')[1:]:
						line+=a.strip('[]')
						if value.split(',')[-1] != a:
							line+=","
					line+=')'
				else:
					line="_".join(words)+"('%s')"%str(value)
			else:
				line="_".join(words)+"()"
		else:
			line='_'.join(words)
	if len(line.split(' '))<=1 and len(line.split('('))<=1:
		print('True')
		line+="()"
	runner(line)
shell()
clear()
get()
