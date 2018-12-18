import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import linspace, sinh
x= linspace(0, 7, 70)
y= sinh(x/2)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sinh(x:2)$')
plt.plot(x, y)
plt.plot(x, y, color = "#FF0000")

plt.show()
