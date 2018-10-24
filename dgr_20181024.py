>
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-6-4564357dd108> in <module>()
      3     if line == 'done':
      4         break
----> 5     print(line)
      6 print('done')
      7 

KeyboardInterrupt: 

In [7]: while True:
   ...:     line=input('>')
   ...:     if line == 'done':
   ...:         break
   ...:     print(line)
   ...: print('done')
   ...:      
>hello
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-e3e4ba4aa9a1> in <module>()
      1 while True:
----> 2     line=input('>')
      3     if line == 'done':
      4         break
      5     print(line)

<string> in <module>()

NameError: name 'hello' is not defined

In [8]: while True:
   ...:     line=input('> ')
   ...:     if line == 'done':
   ...:         break
   ...:     print(line)
   ...: print('done')
   ...:      
> 
  File "<string>", line unknown
    
    ^
SyntaxError: unexpected EOF while parsing


In [9]: while True:
   ...:     line=input('> ')
   ...:         if line == 'done':
   ...:         break
   ...:      fa=str(line)
   ...:      print(fa)
   ...: print('done')
   ...:      
  File "<ipython-input-9-1e890b92aa09>", line 3
    if line == 'done':
    ^
IndentationError: unexpected indent


In [10]: while True:
    ...:     line=input('> ')
    ...:     if line == 'done':
    ...:         break
    ...:      fa=str(line)
    ...:      print(fa)
    ...: print('done')
    ...:      
  File "<ipython-input-10-6621abe99e53>", line 5
    fa=str(line)
                ^
IndentationError: unindent does not match any outer indentation level


In [11]: while True:
    ...:     line=input('> ')
    ...:     if line == 'done':
    ...:         break
    ...:     fa=str(line)
    ...:     print(fa)
    ...: print('done')
    ...:      
> hello 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-11-ea906ac77b83> in <module>()
      1 while True:
----> 2     line=input('> ')
      3     if line == 'done':
      4         break
      5     fa=str(line)

<string> in <module>()

NameError: name 'hello' is not defined

In [12]: while True:
    ...:     line=module('> ')
    ...:     if line == 'done':
    ...:         break
    ...:     fa=str(line)
    ...:     print(fa)
    ...: print('done')
    ...:      
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-12-f9f9952a7f7e> in <module>()
      1 while True:
----> 2     line=module('> ')
      3     if line == 'done':
      4         break
      5     fa=str(line)

NameError: name 'module' is not defined

In [13]: while True:
    ...:     line=input('> ')
    ...:     if line == 'done':
    ...:         break
    ...:     fa=str(line)
    ...:     print(fa)
    ...: print('done')
    ...:      
> he 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-13-ea906ac77b83> in <module>()
      1 while True:
----> 2     line=input('> ')
      3     if line == 'done':
      4         break
      5     fa=str(line)

<string> in <module>()

NameError: name 'he' is not defined

In [14]: while True:
    ...:     line=input('> ')
    ...:     if line == 'done':
    ...:         break
    ...:     fa=str(line)
    ...:     print(fa)
    ...: print('done')
    ...:      
> done
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-14-ea906ac77b83> in <module>()
      1 while True:
----> 2     line=input('> ')
      3     if line == 'done':
      4         break
      5     fa=str(line)

<string> in <module>()

NameError: name 'done' is not defined

In [15]: while True:
    ...:     line=input('> ')
    ...:     if line == 'done':
    ...:         break
    ...:     fa=str(line)
    ...:     print(fa)
    ...: print('done')
    ...:      
> 'done'
done

In [16]: while True:
    ...:     line=input('> ')
    ...:     if line == 'done':
    ...:         break
    ...:     fa=str(line)
    ...:     print(fa)
    ...: print('done')
    ...:      
> 'hello'
hello
> 'done'
done

In [17]: while True:
    ...:     line=input('>' ' ')
    ...:     if line == 'done':
    ...:         break
    ...:     fa=str(line)
    ...:     print(fa)
    ...: print('done')
    ...:      
> hello
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-f2c1adacda26> in <module>()
      1 while True:
----> 2     line=input('>' ' ')
      3     if line == 'done':
      4         break
      5     fa=str(line)

<string> in <module>()

NameError: name 'hello' is not defined

In [18]: while True:
    ...:     line =input('> ')
    ...:     if line[0]=='#':
    ...:         continue
    ...:     if line =='done':
    ...:         break
    ...:     print(line)
    ...: print('done')
    ...:   
> 'hello'
hello
> #'hello man'
  File "<string>", line 1
    #'hello man'
               ^
SyntaxError: unexpected EOF while parsing


In [19]: while True:
    ...:     line =input('> ')
    ...:     if line[0]=='#':
    ...:         continue
    ...:     if line =='done':
    ...:         break
    ...:     print(line)
    ...: print('done')
    ...:   
> '# hello there'
> 'done'
done

In [20]: for i in[5,4,3,2,1]:
    ...:     print(i)
    ...: print('blastofff')
    ...:     
5
4
3
2
1
blastofff

In [21]: draugi = ['ints', 'ints1','ints2']
    ...: for draugs in draugi:
    ...:     print('laimigu jauno gadu:', draugs)
    ...: print('done')
    ...:     
('laimigu jauno gadu:', 'ints')
('laimigu jauno gadu:', 'ints1')
('laimigu jauno gadu:', 'ints2')
done

In [22]: draugi = ['ints', 'ints1','ints2']
    ...: for draugs in draugi:
    ...:     print 'laimigu jauno gadu:' draugs
    ...: print('done')
    ...:     
  File "<ipython-input-22-22d044e9441e>", line 3
    print 'laimigu jauno gadu:' draugs
                                     ^
SyntaxError: invalid syntax


In [23]: draugi = ['ints', 'ints1','ints2']
    ...: for draugs in draugi:
    ...:     print( 'laimigu jauno gadu:' draugs)
    ...: print('done')
    ...:     
  File "<ipython-input-23-9c779c333cc4>", line 3
    print( 'laimigu jauno gadu:' draugs)
                                      ^
SyntaxError: invalid syntax


In [24]: draugi = ['ints', 'ints1','ints2']
    ...: for draugs in draugi:
    ...:     print( 'laimigu jauno gadu:', draugs)
    ...: print('done')
    ...:     
('laimigu jauno gadu:', 'ints')
('laimigu jauno gadu:', 'ints1')
('laimigu jauno gadu:', 'ints2')
done

In [25]: print('begoe')
    ...: for thing in [9,42,12,3,74,15]:
    ...:     print(thing)
    ...: print('after')
    ...:     
begoe
9
42
12
3
74
15
after

In [26]: largest_so_far = =-1
  File "<ipython-input-26-954821dee0b6>", line 1
    largest_so_far = =-1
                     ^
SyntaxError: invalid syntax


In [27]: latgest_so_far = -1 
    ...: print('before', largest_so_far)
    ...: for the_num in[9,41,12,3,74,15]:
    ...:     if the_num > largest_so_far:
    ...:         largest_so_far = the_num
    ...:     print(largest_so_far, the_num)
    ...: print('after', largest _so_far)        
  File "<ipython-input-27-2383143020b1>", line 7
    print('after', largest _so_far)
                                 ^
SyntaxError: invalid syntax


In [28]: 

In [28]: latgest_so_far = -1 
    ...: print('before', largest_so_far)
    ...: for the_num in[9,41,12,3,74,15]:
    ...:     if the_num > largest_so_far:
    ...:         largest_so_far = the_num
    ...:     print(largest_so_far, the_num)
    ...: print('after', largest_so_far )
    ...:         
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-28-49cc9ecec8ad> in <module>()
      1 latgest_so_far = -1
----> 2 print('before', largest_so_far)
      3 for the_num in[9,41,12,3,74,15]:
      4     if the_num > largest_so_far:
      5         largest_so_far = the_num

NameError: name 'largest_so_far' is not defined

In [29]: largest_so_far = -1 
    ...: print('before', largest_so_far)
    ...: for the_num in[9,41,12,3,74,15]:
    ...:     if the_num > largest_so_far:
    ...:         largest_so_far = the_num
    ...:     print(largest_so_far, the_num)
    ...: print('after', largest _so_far)        
  File "<ipython-input-29-f593c9e7ede9>", line 7
    print('after', largest _so_far)
                                 ^
SyntaxError: invalid syntax


In [30]: 

In [30]: largest_so_far = -1 
    ...: print('before', largest_so_far)
    ...: for the_num in[9,41,12,3,74,15]:
    ...:     if the_num > largest_so_far:
    ...:         largest_so_far = the_num
    ...:     print(largest_so_far, the_num)
    ...: print('after', largest_so_far)
    ...:         
('before', -1)
(9, 9)
(41, 41)
(41, 12)
(41, 3)
(74, 74)
(74, 15)
('after', 74)

In [31]: zork = 0

In [32]: print('before')
before

In [33]: print('before', zork)
('before', 0)

In [34]: print('before', zork)
    ...: for thing in [9,12,41,3,74,15]:
    ...:     zork=zork+1
    ...:     print(zork,thing)
    ...: print('after',zork) 
    ...:    
('before', 0)
(1, 9)
(2, 12)
(3, 41)
(4, 3)
(5, 74)
(6, 15)
('after', 6)

In [35]: print('before', zork)
    ...: for thing in [9,12,41,3,74,15]:
    ...:     zork=zork+thing
    ...:     print(zork,thing)
    ...: print('after',zork) 
    ...:    
('before', 6)
(15, 9)
(27, 12)
(68, 41)
(71, 3)
(145, 74)
(160, 15)
('after', 160)

In [36]: count = 0

In [37]: count=0
    ...: summa=0
    ...: print('before',count,summa)
    ...: for value in [9,41,12,3,74,14]:
    ...:     count=count+1
    ...:     summa=summa+value
    ...:     print(count,summa,value)
    ...: print('after',count, summa, summa/count)
    ...:     
('before', 0, 0)
(1, 9, 9)
(2, 50, 41)
(3, 62, 12)
(4, 65, 3)
(5, 139, 74)
(6, 153, 14)
('after', 6, 153, 25)

In [38]: count=0
    ...: summa=0
    ...: print('before',count,summa)
    ...: for value in [9,41,12,3,74,14]:
    ...:     count=count+1
    ...:     summa=summa+value
    ...:     print(count,summa,value)
    ...: print('after',count summa summa/count)
    ...: 
    ...:     
  File "<ipython-input-38-4fa000b13ff7>", line 8
    print('after',count summa summa/count)
                            ^
SyntaxError: invalid syntax


In [39]: print("before")
    ...: for value in [9,41,12,3,74,15]:
    ...:     if value>20:
    ...:         print("liels cipars", value)
    ...: print("After")
    ...:         
before
('liels cipars', 41)
('liels cipars', 74)
After

In [40]: found = False
    ...: print("before", found)
    ...: for value in [9,41,12,3,74,15]:
    ...:     if value==3:
    ...:         found = True
    ...:         print(found, value)
    ...: print("After", found)
    ...: 
    ...:         
('before', False)
(True, 3)
('After', True)

In [41]: smallest = None

In [42]: print('before')
    ...: for value in p[9,41,12,3,74,15]:
    ...:     if smallest is None:
    ...:         smallest = value
    ...:     elif value < smallest:
    ...:         smallest= value
    ...:     print(smallest,value)
    ...: print('after', smallest)
    ...:             
before
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-42-e98b64a30428> in <module>()
      1 print('before')
----> 2 for value in p[9,41,12,3,74,15]:
      3     if smallest is None:
      4         smallest = value
      5     elif value < smallest:

NameError: name 'p' is not defined

In [43]: print('before')
    ...: for value in [9,41,12,3,74,15]:
    ...:     if smallest is None:
    ...:         smallest = value
    ...:     elif value < smallest:
    ...:         smallest= value
    ...:     print(smallest,value)
    ...: print('after', smallest)
    ...:             
before
(9, 9)
(9, 41)
(9, 12)
(3, 3)
(3, 74)
(3, 15)
('after', 3)

