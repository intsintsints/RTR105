In [1]: open("history_20180912_.txt", "r")
   ...: 
   ...: 
Out[1]: <_io.TextIOWrapper name='history_20180912_.txt' mode='r' encoding='UTF-8'>

In [2]: stuff = "hello\nWorld!"

In [3]: stuff
Out[3]: 'hello\nWorld!'

In [4]: stuff = "hello \n World!"

In [5]: stuff
Out[5]: 'hello \n World!'

In [6]: print(stuff)
hello 
 World!

In [7]: stuff = "hello\nWorld!"

In [8]: print(stuff)
hello
World!

In [9]: len(stuff)
Out[9]: 12


[2]+  Stopped                 ipython
user@epk428-20:~/RTR105$ nano text.txt
user@epk428-20:~/RTR105$ ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: failsfails = open("text.txt")

In [2]: failsfails
Out[2]: <_io.TextIOWrapper name='text.txt' mode='r' encoding='UTF-8'>

In [3]: failsfails.read
Out[3]: <function TextIOWrapper.read>

In [4]: failsfails.read()
Out[4]: 'teksts\n'

In [5]: failsfails.seek()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-ac9c3fa67558> in <module>()
----> 1 failsfails.seek()

TypeError: seek() takes at least 1 argument (0 given)

In [6]: failsfails.seek(1)
   ...: 
Out[6]: 1

In [7]: failsfails.read()
Out[7]: 'eksts\n'

In [8]: xfile = open("text.txt")
   ...: for s in xfile
  File "<ipython-input-8-92942a203c79>", line 2
    for s in xfile
                  ^
SyntaxError: invalid syntax


In [9]: xfile = open("text.txt")
   ...: for s in xfile:
   ...:     print(s)
   ...:     
teksts


In [10]: xfile = open("text.txt")
    ...: for s in xfile:
    ...:     print(s)
    ...:     
    ...:     
teksts


In [11]: rskaits = open("text.txt
  File "<ipython-input-11-0e9719699a67>", line 1
    rskaits = open("text.txt
                            ^
SyntaxError: EOL while scanning string literal


In [12]: rskaits = open("text.txt
  File "<ipython-input-12-0e9719699a67>", line 1
    rskaits = open("text.txt
                            ^
SyntaxError: EOL while scanning string literal


In [13]: rskaits = open("text.txt")
    ...: count=0
    ...: for line in rskaits:
    ...:     count=count+1
    ...: print("rindu skaits:, count)    
  File "<ipython-input-13-d2f23599de24>", line 5
    print("rindu skaits:, count)
                                    ^
SyntaxError: EOL while scanning string literal


In [14]: 

In [14]: rskaits = open("text.txt")
    ...: count=0
    ...: for line in rskaits:
    ...:     count=count+1
    ...: print("rindu skaits":, count)    
  File "<ipython-input-14-fa19764137ef>", line 5
    print("rindu skaits":, count)
                        ^
SyntaxError: invalid syntax


In [15]: rskaits = open("text.txt")
    ...: count=0
    ...: for line in rskaits:
    ...:     count=count+1
    ...: print("rindu skaits:", count) 
    ...:    
rindu skaits: 1

In [16]: rskaits = open("text.txt")
    ...: count=0
    ...: for lin in rskaits:
    ...:     count=count+1
    ...: print("rindu skaits:", count) 
    ...:    
rindu skaits: 1

In [17]: rskaits = open("text.txt")
    ...: count=0
    ...: for lin in rskaits:
    ...:     count=count+1
    ...: print("rindu skaits:", count) 
    ...:    
rindu skaits: 1

In [18]: tt=open("text.txt")
    ...: inp=tt.read()
    ...: print(len(inp))
    ...: 
7

In [19]: print(inp[:4])
teks

In [20]: mip=open("text.txt")
    ...: for line in mip:
    ...:     if line.startswith("re:"):
    ...:         print(line)
    ...:         

In [21]: mip=open("text.txt")
    ...: for line in mip:
    ...:     if line.startswith("te:"):
    ...:         print(line)
    ...:         

In [22]: mip=open("text.txt")
    ...: for line in mip:
    ...:     if line.startswith("te"):
    ...:         print(line)
    ...:         
teksts


In [23]: 

In [23]: mip=open("text.txt")
    ...: for line in mip:
    ...:     line = line.rstrip()
    ...:     if not line.startswith("from:"):
    ...:         continue
    ...:     print(line)
    ...:         

In [24]: mip=open("text.txt")
    ...: for line in mip:
    ...:     line = line.rstrip()
    ...:     if not line.startswith("te"):
    ...:         continue
    ...:     print(line)
    ...:         
teksts

In [25]: fname= input("ieraksti faila vardu: ")
    ...: fopen=open(fname)
    ...: count=0
    ...: for line in fopen:
    ...:     if line.startswith("te"):
    ...:         count=count+1
    ...: print("bija",count,"rindas",fname,"ā")
    ...:         
ieraksti faila vardu: text.txt
bija 1 rindas text.txt ā

In [26]: fname= input("ieraksti faila vardu: ")
    ...: try:
    ...:     fopen=open(fname)
    ...: except:
    ...:     print("faila nav")
    ...:     quit()
    ...:     
    ...: count=0
    ...: for line in fopen:
    ...:     if line.startswith("te"):
    ...:         count=count+1
    ...: print("bija",count,"rindas",fname,"ā")
    ...:         
ieraksti faila vardu: jaska
faila nav
bija 0 rindas jaska ā
user@epk428-20:~/RTR105$ 

