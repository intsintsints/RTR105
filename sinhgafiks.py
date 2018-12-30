import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import linspace, sinh

def f1(x):
    return x**1/(2)

def f2(x):
    return f1(x) * x*x/((2)*(2+1)*2**2)

def f3(x):
    return f2(x) * x*x/((2*2)*(2*2+1)*2**2)

def f4(x):
    return f3(x) * x*x/((2*3)*(2*3+1)*2**2)


x= linspace(0, 7, 70)
y= sinh(x/2)

y1 = f1(x)
y2 = f2(x)
y3 = f3(x)
y4 = f4(x)

legend = []


from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sinh(x:2)$ un taas izvirziijumi rindaa')
plt.plot(x, y, color = "#FF0000")
legend.append("$sinh(x/2)$")
plt.plot(x,y1,color = "#FF00FF")
legend.append("$f1(x)$")                    
plt.plot(x,y2,color = "#00FF00")
legend.append("$f2(x)$")
plt.plot(x,y3,color = "#0000FF")
legend.append("$f3(x)$")
plt.plot(x,y4,color = "#FFFF00")
legend.append("$f4(x)$")
plt.legend(legend, loc = 2)
plt.show()

plt.show()


