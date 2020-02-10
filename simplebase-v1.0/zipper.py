
from zipfile import ZipFile
from shutil import make_archive
import sys
import os


commands  = sys.argv

#print(commands)
def start():
      if len(commands)==1:
          print("Usage : python zipper.py zipname files")
          return
      if commands[-1].lower() == 'r':
          if commands[-2].lower() == 'f':
              reader(commands[2])
          else:
              reader()
              
      elif commands[-1].lower()=='w':
          writer(commands[-2],f=commands[2])
          
      elif commands[-1].lower()=='e':
          if commands[-2]=='f':
              extract(commands[2])
            
          else:
              extract()
      else:
          make()
          
def make():
      path  = os.path.split(commands[0])
      print("Building %s.zip"%commands[1])
      #make_archive(commands[1],'zip',path[0])

      with ZipFile(commands[1]+'.zip','w') as z:
          for f in commands[2:]:
            print('Writing %s...'%f)
            z.write(os.path.join(path[0],f))
            os.remove(os.path.join(path[0],f))

      print("Zip File %s.zip Built Successfully..."%commands[1])

def extract(f=''):
      with ZipFile(sys.argv[1]+".zip",'r') as z:
        if f:
          z.extract('%s.txt'%f)
          
        else:
          z.extractall()
        print("Extract Successfully!")

def reader(f=''):
      path=os.path.split(sys.argv[0])
      if f:
        with ZipFile(commands[1]+'.zip','r') as z:
          print(z.read(f+'.txt'))
      else:
        with ZipFile(commands[1]+'.zip','r') as z:
          z.printdir()
def writer(text,f=''):
      path=os.path.split(sys.argv[0])[0]
      print("trying to manipulate %s.txt, adding \"%s\""%(f,text))
      with ZipFile(commands[1]+'.zip','a') as z:
        for file in z.namelist():
          print(file)
          if file.lower()=='%s.txt'%f:
            print("found file %s"%f)
            with open(file,'w') as f:
              f.write("{t}".format(t=text))
              f.close()
              print("-"*30,"\n")
              print('Written Successfully to %s'%f)
start()




