
In [1]: str1="hello"

In [2]: str2="ints"

In [3]: tg = str1 + str2

In [4]: print(tg)
helloints

In [5]: str3="123"

In [6]: str3= str3 +1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-d532574409a8> in <module>()
----> 1 str3= str3 +1

TypeError: must be str, not int

In [7]: f= int(str3) +2

In [8]: print(f)
125

In [9]: vards = input("ievadi
  File "<ipython-input-9-883ca2e69284>", line 1
    vards = input("ievadi
                         ^
SyntaxError: EOL while scanning string literal


In [10]: vards = input("ievadi:")
ievadi:ints

In [11]: print(vards)
ints

In [12]: aboli=input("ievadi:")
ievadi:50

In [13]: x=aboli-2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-13-58fa3fd12ebd> in <module>()
----> 1 x=aboli-2

TypeError: unsupported operand type(s) for -: 'str' and 'int'

In [14]: x=int(aboli)-2

In [15]: print(x)
48

In [16]: auglis="bumbieris"

In [17]: letter=auglies[3]
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-cd3566fda42b> in <module>()
----> 1 letter=auglies[3]

NameError: name 'auglies' is not defined

In [18]: letter=auglis[3]

In [19]: print(letter)
b

In [20]: m=3

In [21]: w=auglis[m-2]

In [22]: print(w)
u

In [23]: print(len(auglis))
9

In [24]: index=0

In [25]: while index<len(auglis):
    ...:     letter=auglis[index]
    ...:     print(index,letter)
    ...:     index=index+1
    ...:     
0 b
1 u
2 m
3 b
4 i
5 e
6 r
7 i
8 s

In [26]: for letter in auglis:
    ...:     print(letter)
    ...:     
b
u
m
b
i
e
r
i
s

In [27]: index=0
    ...: while index<len(auglis):
    ...:     letter=auglis[index]
    ...:     print(letter)
    ...:     index=index+1
    ...:     
b
u
m
b
i
e
r
i
s

In [28]: word="bumbieris"

In [29]: word="bumbieris":
  File "<ipython-input-29-9ba1f9a6c1d8>", line 1
    word="bumbieris":
                    ^
SyntaxError: invalid syntax


In [30]: word="bumbieris
  File "<ipython-input-30-8f2d8b5027d8>", line 1
    word="bumbieris
                   ^
SyntaxError: EOL while scanning string literal


In [31]: word="bumbieris"

In [32]: count=0


[1]+  Stopped                 ipython
user@epk428-20:~/RTR105$ ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: vards="bumbieris"

In [2]: count=0

In [3]: for letter in word:
   ...:     if letter =="b":
   ...:         count=count+1
   ...: print(count)
   ...:         
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-3-2190f1d3859e> in <module>()
----> 1 for letter in word:
      2     if letter =="b":
      3         count=count+1
      4 print(count)
      5 

NameError: name 'word' is not defined

In [4]: for letter in vards:
   ...:     if letter =="b":
   ...:         count=count+1
   ...: print(count)
   ...:         
2

In [5]: s="Monthy Python"

In [6]: print(s[0:4])
Mont

In [7]: print(s[6:100])
 Python

In [8]: print(s[:])
Monthy Python

In [9]: a="sveiks"

In [10]: b=a+" "+"ints"

In [11]: print(b)
sveiks ints

In [12]: 

In [12]: auglis="bumbieris"

In [13]: m in auglis
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-13-ff7b34bcadbd> in <module>()
----> 1 m in auglis

NameError: name 'm' is not defined

In [14]: "m" in auglis
Out[14]: True

In [15]: "n" in auglis
Out[15]: False

In [16]: if "m" in auglis:
    ...:     print("intsintsints")
    ...:     
intsintsints

In [17]: if word == "bumbieris":
    ...:     print("čau, bumbieris.")
    ...:     
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-f2301cc4de4e> in <module>()
----> 1 if word == "bumbieris":
      2     print("čau, bumbieris.")
      3 

NameError: name 'word' is not defined

In [18]: if word == "bumbieris":
    ...:     print("čau, bumbieris.")
    ...:     
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-18-f2301cc4de4e> in <module>()
----> 1 if word == "bumbieris":
      2     print("čau, bumbieris.")
      3 

NameError: name 'word' is not defined

In [19]: if vards  == "bumbieris":
    ...:     print("čau, bumbieris.")
    ...:     
čau, bumbieris.

In [20]: if vards < "bumbieris":
    ...:     print("tavs vards," + vards+", iet pirms bumbieris.")
    ...: elif vards > " bumbieris":
    ...:     print("tavs vards," +vards+", iet pec bumbiera.")
    ...: else:
    ...:     print("čau bumbieris.")
    ...:             
tavs vards,bumbieris, iet pec bumbiera.

In [21]: if vards < "bumbieris":
    ...:     print("tavs vards," + vards+", iet pirms bumbieris.")
    ...: elif vards > "bumbieris":
    ...:     print("tavs vards," +vards+", iet pec bumbiera.")
    ...: else:
    ...:     print("čau bumbieris.")
    ...:             
čau bumbieris.

In [22]: greet = "cau ints"

In [23]: zap = greet.lower()

In [24]: print(zap)
cau ints

In [25]: greet="CAu INTs"

In [26]: print(zap)
cau ints

In [27]: lieta="cau zeme"

In [28]: type(lieta)
Out[28]: str

In [29]: dir(lieta)
Out[29]: 
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']

In [30]: vards="bumbieris"

In [31]: pos = vards.find("b")

In [32]: print(pos)
0

In [33]: pos = vards.find("ie")

In [34]: print(pos)
4

In [35]: pos = vards.find("ied")

In [36]: print(pos)
-1

In [37]: greet="cau ints"

In [38]: nnn=greet.upper()

In [39]: print(nnn)
CAU INTS

In [40]: nstr=greet.replace("ints","janis")

In [41]: print(nstr)
cau janis

In [42]: dfg=nstr.replace("a","B")

In [43]: print(dfg)
cBu jBnis

In [44]: greet=" cau ints     "

In [45]: greet.instrip()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-45-3898fd0139e0> in <module>()
----> 1 greet.instrip()

AttributeError: 'str' object has no attribute 'instrip'

In [46]: greet.lnstrip()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-46-45716e69e04f> in <module>()
----> 1 greet.lnstrip()

AttributeError: 'str' object has no attribute 'lnstrip'

In [47]: greet.lstrip()
Out[47]: 'cau ints     '

In [48]: greet.rstrip()
Out[48]: ' cau ints'

In [49]: greet.strip()
Out[49]: 'cau ints'

In [50]: line="jauku dienu"

In [51]: line.startswith("jauku")
Out[51]: True

In [52]: line.startswith("J")
Out[52]: False

In [53]: 

