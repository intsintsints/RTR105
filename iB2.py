# -*- coding: utf-8 -*-
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from math import sin
from numpy import linspace

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 4:

        k = k + 1
        
        R = (-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

        
    print("Izdruka no liet.f. Beigas!")
    return S
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = sin(x)
print("standarta sin(%.2f) = %6.2f"%(x,y))
yy = mans_sinuss(x)
print("mans sin(%.2f) = %6.2f"%(x,yy))
m=0
while m<4:
    m=m+1  
    S = linspace(0, 7, 70)
    y=mans_sinuss(S)
    from matplotlib import pyplot as plt
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Funkcija $sin(x)$')
    plt.plot(S, y)
    plt.plot(S, y, color = "#FF0000")
    plt.show() 

