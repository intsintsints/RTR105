Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print("intsintsints")
intsintsints
>>> x=12.2
>>> print(x)
12.2
>>> x=12.2
>>> x=24
>>> print(x)
24
>>> print(x)
24
>>> spams=45
>>> print(spams)
45
>>> 24iki
SyntaxError: invalid syntax
>>> 24iki=454
SyntaxError: invalid syntax
>>> *frgr=7
SyntaxError: invalid syntax
>>> q=2
>>> h=7
>>> c=q*h
>>> print(c)
14
>>> x=2
>>> x=x+2
>>> print(x)
4
>>> x=3.9*x*(4-x)
>>> print(X)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined
>>> print(x)
0.0
>>> x=45*x*(5+x)
>>> print(x)
0.0
>>> jj=47
>>> kk=jj%4
>>> print(kk)
3
>>> print(7**5)
16807
>>> 1+2*3-4/5**6
7
>>> 5**6
15625
>>> 4/15625
0
>>> 7/(4/15625)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    7/(4/15625)
ZeroDivisionError: integer division or modulo by zero
>>> 2./15625.
0.000128
>>> x=4
>>> x=float(x)
>>> type(x)
<type 'float'>
>>> print(float(78) + 56)
134.0
>>> i = 45
>>> type (i)
<type 'int'>
>>> y='34'
>>> type(y)
<type 'str'>
>>> print(1+y)

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(1+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> jug = int(y)
>>> print(1+y)

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(1+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(jug+1)
35
>>> vards = input("Kas tu esi?")
Kas tu esi?

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    vards = input("Kas tu esi?")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> vards = input ('Kas tu esi?')
Kas tu esi? Ints

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    vards = input ('Kas tu esi?')
  File "<string>", line 1, in <module>
NameError: name 'Ints' is not defined
>>> vards = input('Kas tu esi?') print ('Welcome', vards)
SyntaxError: invalid syntax
>>> vards = input("Kas tu esi?")
Kas tu esi? 

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    vards = input("Kas tu esi?")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
>>> vards = input("Kas tu esi?")
Kas tu esi? INts

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    vards = input("Kas tu esi?")
  File "<string>", line 1, in <module>
NameError: name 'INts' is not defined
>>> vards = raw_input("kas tu esi?")
kas tu esi? Ints
>>> print ("welcome", vards)
('welcome', ' Ints')
>>> print('welcome', vards)
('welcome', ' Ints')
>>> print welcome vards
SyntaxError: invalid syntax
>>> print('welcome %s'%vards)
welcome  Ints
>>> 
==================== RESTART: /home/user/RTR105/test2.py ====================
Kas tu esi? ints
welcome  ints
>>> inp = raw_input("EU floor?")
EU floor?
>>> lvf = int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    lvf = int(inp) + 1
ValueError: invalid literal for int() with base 10: ''
>>> 
