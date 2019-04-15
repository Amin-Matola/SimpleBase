import os,subprocess,sys
from zipfile import ZipFile
import time
from colorama import Back,Fore


name=''

main_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
path=os.path.join(main_dir,'databases')
recpath=''

shell_colors = [(Back.LIGHTMAGENTA_EX+Fore.LIGHTWHITE_EX)]
def shell():
	for m in shell_colors:
		print(m)
		


def create_database(name):
	if not os.path.exists(path):
		os.mkdir(path)
	os.chdir(path)
	os.mkdir(name)

def show_databases():
	folders=[]
	for dirp,dirn,fs in os.walk(path):
		for a in dirn:
			folders.append(a)
		break
	
	print(".-------------------------------.")
	print("|  Databases    \t\t|")
	print("|-------------------------------|")
	if len(folders):
		for a in folders:
			if len(a)>=4:
				if len(a)>=4 and len(a)<=10:
					print("|  ",a,"\t\t\t|")
				elif len(a)>=20:
					print("|  ",a,"\t|")
				else:
					print("|  ",a,"\t\t|")
			elif len(a)==1:
				print("|  ",a," \t\t\t\t|")

			else:
				print("|  ",a," \t\t|")
	else:
		print("| No databases found!\t\t|")

	print("|_______________________________|")


def use_database(name):
	global recpath
	recpath=os.path.join(path,name)
	print('  Database changed, %s used!'%name)
	
def drop_database(name):
	dpath=os.path.join(path,name)
	for a,b,c in os.walk(dpath):
		for f in c:
			os.remove(os.path.join(dpath,f))
		break
	os.rmdir(dpath)
	print("  Database %s deleted!"%name)

def show_tables():
	files=[]
	if not recpath:
		print('  No database selected!')
		return
	for dirp,dirnames,file in os.walk(recpath):
		for f in file:
			if str(f).endswith('.csv'):
				files.append(f.split(".")[0])
		break
	print(".-------------------------------.")
	print("|  Tables    \t\t\t|")
	print("|-------------------------------|")
	if len(files):
		for a in files:
			if len(a)>=4:
				if len(a)>=4 and len(a)<=10:
					print("|  ",a,"\t\t\t|")
				elif len(a)>=20:
					print("|  ",a,"\t|")
				else:
					print("|  ",a,"\t\t|")
			elif len(a)==1:
				print("|  ",a," \t\t\t\t|")

			else:
				print("|  ",a," \t\t\t|")
	else:
		print("| No tables found!\t\t|")

	print("|_______________________________|")

def desc_table(name):
	use(name)
	select_all(n=0)

def use(n):
	global name
	name=n

def op():
	f=open(os.path.join(recpath,name+'.csv'),'r+')
	return f

def create_table(table,*args):
	if len(table)>25:
		print(" Table names can not be more than 25 characters!")
		return
	file=os.path.join(recpath,table+'.csv')
	open(file.strip("\'"),'x').close()

	f=open(file,'r+')
	f.seek(0,0)
	names=[str(a)[::-1]+"," for a in args[0:]]
	names[-1]=names[-1].strip(',')+"\n"
	f.writelines(names)
	f.close()
	print(" Table %s created"%table)
		

def insert_into(table,*args):
	if table:
		use(table)
	f=op()
	f.seek(0,2)
	l=["%s,"%(str(b)[::-1].strip('[]')) for b in args]
	l[-1]=l[-1].strip(',[]')+"\n"
	f.writelines(l)
	f.close()	
	print(" ",1," rows affected!")

def insert_all(table,*args):
	if table:
		use(table)
	f=op()
	for a in args:
		f.seek(0,2)
		l=["%s,"%(str(b)[::-1].strip('[]')) for b in a]
		l[-1]=l[-1].strip(',[]')+"\n"
		f.writelines(l)
	f.close()	
	print(" ",len(args)," rows affected!")

def update_table(table,column,fvalue='',lvalue=''):
	li=''
	if table:
		use(table)
	f=op()
	data=f.readlines()
	lists1=[str(a).strip().split(",") for a in data]
	lists=[str(a)[::-1] for a in lists1[0]]
	c=lists.index(column)
	for d in range(len(lists1)):
		if d==0:
			pass
		lists1[d]=[a[::-1] for a in lists1[d]]
		#print(lists1[d])
		if str(lists1[d][c])==str(fvalue):
			lists1[d][c]=str(lvalue)
			print(' Update %s successful!'%column)
		else:
			pass
		lists1[d]=[a[::-1] for a in lists1[d]]

	open(os.path.join(recpath,table+'.csv'),'w').close()
	for l in lists1:
		f=open(os.path.join(recpath,table+'.csv'),'a+')
		#f.seek(0,0)
		f.writelines(','.join(l).strip(','))
		f.write('\n')

def select_all(table='',n=''):
	if table:
		use(table)
	f=op()
	if n==0:
		data=[f.readlines()[0]];
	else:
		data=f.readlines()
	if len(data)<1:
		print(" No table created!")
		return
	lists=[str(a).strip().split(",") for a in data]
	headers=lists[0]

	print("\n\t\tThe %s Record"%(table or name))
	print("."+"_"*(18*len(headers)-1)+'.')
	ls="|ID"
	ls1=["   \t %s"%i[::-1] for i in headers]
	for i in ls1:
		ls+=i
	if len(ls.split('\t')[-1])>=10:
		print(ls+"\t\t|")
	else:
		print(ls+"\t\t|")

	print("|"+'-'*(18*len(headers)-1)+'|')
	a=0
	if len(lists)>0:
		for i in range(len(lists)):
			if i==0:
				continue
			else:
				l=""
				if len(lists[i][0])<=5:
					lis=["   \t|%s"%(str(b)[::-1]) for b in lists[i]]

					for k in lis:
						l+=k
					rec =l.split('\t')
					if len(rec[-1].strip())>10:
						print("|",i,l+' \t|')
					else:
						if len(rec[-2].strip())>9 and len(rec[-1])>=9:
							print("|",i,l+' \t|')
						else:
							print("|",i,l+' \t|')
					
				else:
					lis=["   \t|%s"%(str(b)[::-1]) for b in lists[i]]
					for k in lis:
						l+=k
					rec =l.split('\t')
					if len(rec[-1].strip())>10:
						print("|",i,l+' \t|')
					else:
						if len(rec[-2].strip())>9 and len(rec[-1])>=9:
							print("|",i,l+' \t|')
						else:
							print("|",i,l+' \t|')
				
				print("|"+'_'*(18*len(headers)-1)+"|")
	print(" ",len(data)-1,"rows affected!")
	f.close()

def delete(*c):
	f=op()
	data=f.readlines();
	f.close()
	rpath[-1]=name
	path="\\".join(rpath)+".csv"
#	os.remove(r"db.csv")
	path=os.path.join(recpath,name+'.csv')
	open(path,'w').close()

	f=op()
	for i in range(len(c)):
		data.pop(i+1)
	f.seek(0,0)
	f.writelines(data)
	print(' %d row affected!'%len(c))

def clear():
	if sys.platform=='win32':
			os.system("cls")
	else:
			os.system('clear')
	print(" Simple Base Version 0.1.0, Initial Release On %s (Version %s.%s.%s)."%(os.sys.platform,
	os.sys.getwindowsversion().platform_version[0],
	os.sys.getwindowsversion().platform_version[1],
	os.sys.getwindowsversion().platform_version[2]))
	print(" "+time.ctime(),"(%s)"%time.tzname[0])
	print("*"*75+"\n")

def drop_table(tb):
	path=os.path.join(recpath,tb+'.csv')
	print(" Deleting %s..."%tb)
	os.remove(path)
	print(' Table %s deleted!'%tb)
	
