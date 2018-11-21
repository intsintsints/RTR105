import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import cos,linspace, sin
x= linspace(0, 7, 70)
y= cos(x)
y2 = sin(x)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x, y)
plt.plot(x, y, color = "#FF0000")
plt.plot(x,y2)
plt.show()
