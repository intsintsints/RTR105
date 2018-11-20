# -*- coding: utf-8 -*-
from math import sinh
def mans_hsinuss2(x):
    k = 0
    a = x**1/(2)
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))
    while k < 500:
        k = k + 1
        R = x*x/((2*k)*(2*k+1)*2**2)
        a = a * R
        S = S + a
        if k == 499:
             print("Izdruka no liet.f. a499 = %6.2f S499 = %6.2f"%(a,S))
    print("Izdruka no liet.f. a500 = %6.2f S500 = %6.2f"%(a,S))
    print("Izdruka no liet.f. Beigas!")
    return S
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = sinh(x/2)
print("standarta sin(%.2f) = %6.2f"%(x,y))
yy = mans_hsinuss2(x)
m=u"\u221E"
print("mans sin(%.2f) = %6.2f"%(x,yy))
print(" ")
print("            500")
print("          _______")
print("          \      2*k+1")
print("           \    x")
print("sinh(%.2f/2)=>  __________            D.a. -%s < x < %s "%(x,m,m))
print("           /                2k+1    ")
print("          /____ (2*k+1)! * 2")
print("           k=0")
print(" ")
print("                                2")
print("                               x ")
print("rekurences reizinātājs: _________________")
print("                                         2")
print("                         k*2 * (k*2+1) *2")

