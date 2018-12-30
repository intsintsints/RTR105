# fails : 170.py
# autors : Ints Muraans
# apliecības numurs : 181REB253
# datums : 03 12 2018
# sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding : tf -8 -*-
from math import sinh, fabs
from time import sleep

def f(x):
    return sinh(x/2)

#definejam argumenta x robezhas:
a = 1.1
b = 3.2 

# Aprekjinam argumenta x robezhas:
funa = f(a)
funb = f(b)

# Paarbaudam, vai dtotajaa intervaalaa ir saknes:
if (funa * funb > 0.0):
    print("Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b))
    sleep(1); exit()    # Zinjo uz ekraana, gaida 1 sec. un darbu pabeidz
else:
    print ("Dotajaa intervaalaa sakne(s) ir!")

# Defineejam precizitaati, ar kaadu mekleesim sakni:
deltax = 0.01
# sashaurinam saknes mekleeshanas robezhas:
k=0
while (fabs (b-a) > deltax ):
    k=k+1
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b=x
    else:
        a=x

deffunk = sinh(x/2)

print ("Sakne ir: ", x)
print ("Funkcijas vertiiba ir:", deffunk)
print ("Tik reizes vajadzeeja daliit uz puseem", k)
