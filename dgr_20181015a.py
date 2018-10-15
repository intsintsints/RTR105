

x=5
if xPython 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: x=5

In [2]: if x<10:
   ...:     print ('smaller')
   ...:     
smaller

In [3]: if x>20:
   ...:     print('bigger')
   ...:     

In [4]: if x < 10:
   ...:     print('Smaller')
   ...: if x > 20:
   ...:     print ('Bigger')
   ...: print ('finis')
   ...:     
Smaller
finis

In [5]: x=5

In [6]: if x==5:
   ...:     print('equals 5')
   ...:     
equals 5

In [7]: if x > 4:
   ...:     print('greater than 4')
   ...: if x >=5:
   ...:     print('greater than or equals 5')
   ...: if x <6:
   ...:     print('less than 6')
   ...:             
greater than 4
greater than or equals 5
less than 6

In [8]: if x <=5:
   ...:     print('less than or equals 5')
   ...: if x!=6:
   ...:     print('not equal 6')
   ...:          
less than or equals 5
not equal 6

In [9]: print('before 5')
before 5

In [10]: print("before 5")
    ...: 
    ...: 
before 5

In [11]: x=5

In [12]: print("before 5")
before 5

In [13]: print("before 5")
    ...: if x== 5:
    ...:     print("is 5")
    ...:     print("is still 5")
    ...:     print("third 5")
    ...: print("afterwards 5")
    ...: print("before 6")
    ...: if x == 6:
    ...:     print("is 6")
    ...:     print("is still 6")
    ...:     print("third 6")
    ...: print ("afterwards 6")
    ...:         
before 5
is 5
is still 5
third 5
afterwards 5
before 6
afterwards 6

In [14]: x=42

In [15]: if x> 1:
    ...:     print("more than 1")
    ...:     if x<100:
    ...:         print("less than 100")
    ...: print("all done")
    ...:         
more than 1
less than 100
all done

In [16]: x=4

In [17]: if x>2:
    ...:     print("bigger")
    ...: else:
    ...:     print("smaller")
    ...: print ("all done")
    ...:             
bigger
all done

In [18]: x=20

In [19]: if x < 2:
    ...:     print("small")
    ...: elif x <10:
    ...:     print("medium")
    ...: else:
    ...:     print("large")
    ...: print("all done")
    ...:             
large
all done

In [20]: if x < 2:
    ...:     print("below 2 ")
    ...: elif x< 20:
    ...:     print("below 20")
    ...: elif x< 10:
    ...:     print("below 10" )
    ...: else :
    ...:     print("kkas cits")
    ...:                
kkas cits

In [21]: x=1


[1]+  Stopped                 ipython
user@epk428-20:~/RTR105$ ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: x=1 

In [2]: if x < 2:
   ...:     print("below 2 ")
   ...: elif x< 20:
   ...:     print("below 20")
   ...: elif x< 10:
   ...:     print("below 10" )
   ...: else :
   ...:     print("kkas cits")
   ...:     
below 2 

In [3]: astr = "hello ints"

In [4]: try:istr=int(astr)
   ...: except:
   ...:     istr=-1
   ...: print("first", istr)
   ...:     
first -1

In [5]: astr = "567"

In [6]: try:
   ...:     istr=int(astr)
   ...: except:
   ...:     istr = -1
   ...: print("second", istr)
   ...:         
second 567

In [7]: astr = "ints"

In [8]: try:
   ...:     print("hello")
   ...:     istr = int(astr)
   ...:     print("there")
   ...: except:
   ...:     istr=-2
   ...: print ("done", istr)
   ...:         
hello
done -2

In [9]: print("hello")
   ...: istr = int(astr)
   ...: print("there")
   ...: print ("done", istr)
   ...:         
hello
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-9-a781202e2d20> in <module>()
      1 print("hello")
----> 2 istr = int(astr)
      3 print("there")
      4 print ("done", istr)
      5 

ValueError: invalid literal for int() with base 10: 'ints'

In [10]: kd = input("ievadi ciparu:")
ievadi ciparu:d               

In [11]: try:
    ...:     ed=int(kd)
    ...: except:
    ...:     ed=-1
    ...: if ed > 0:
    ...:     print("        
  File "<ipython-input-11-11d88d0d32e7>", line 6
    print("
                   ^
SyntaxError: EOL while scanning string literal


In [12]: try:
    ...:     ed=int(kd)
    ...: except:
    ...:     ed=-1
    ...: if ed > 0:
    ...:     print("labs darbs")
    ...: else:
    ...:     print("slikts darbs")
    ...:                 
slikts darbs

In [13]: kd = input("ievadi skaili:")
    ...: try:
    ...:     ed=int(kd)
    ...: except:
    ...:     ed=-1
    ...: if ed > 0:
    ...:     print("labs darbs")
    ...: else:
    ...:     print("slikts darbs")
    ...:                 
ievadi skaili:56
labs darbs

In [14]: kd = input("ievadi skaili:")
    ...: try:
    ...:     ed=int(kd)
    ...: except:
    ...:     ed=-1
    ...: if ed > 0:
    ...:     print("labs darbs")
    ...: else:
    ...:     print("slikts darbs")
    ...:                 
ievadi skaili:yt
slikts darbs

In [15]: 

