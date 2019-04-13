import json
from queries import *

colors = [(Back.LIGHTMAGENTA_EX+Fore.LIGHTWHITE_EX)]

name=''
rpath=os.path.abspath(sys.argv[0]).split('\\')
here=rpath.copy()
here[-1]=''
path=os.path.join("\\".join(here),'databases')
recpath=''


def show_to_json(table=''):
	if table:
		use(table)
	f=op()
	data=f.readlines()
	lists1=[str(a).strip().split(",") for a in data]
	lists=[str(a)[::-1] for a in lists1[0]]
	
	#for a in lists:
	all_ = []
	for b in range(len(lists1)):
		if b==0:
			continue
		d={}.fromkeys(lists)
		for i in range(len(d)):
				d[lists[i]]=lists1[b][i][::-1]
		all_.append(d)
	print(json.dumps(all_,indent=2))
def save_to_json(table='',dest=''):
	if dest and not os.path.exists(os.path.abspath(dest)):
		open(dest,'x').close()
	if table:
		use(table)
	f=op()
	data=f.readlines()
	lists1=[str(a).strip().split(",") for a in data]
	lists=[str(a)[::-1] for a in lists1[0]]
	
	#for a in lists:
	all_ = []
	for b in range(len(lists1)):
		if b==0:
			continue
		d={}.fromkeys(lists)
		for i in range(len(d)):
				d[lists[i]]=lists1[b][i][::-1]
		all_.append(d)
	file=open(os.path.abspath(dest),'a+')
	file.writelines(json.dumps(all_,indent=2))
	file.close()
	print(" Json data stored in %s"%dest)