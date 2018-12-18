#print (vars())
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print(vars())

from numpy import sinh, linspace
#print (vars())

def f(x):
    return sinh(x/2)


x=linspace(0,4,11)
#print (vars())

y=sinh(x/2)

legend = []
#print (legend)

from matplotlib import pyplot as plt
#print()plt._doc_)
plt.axis([-1, 6, -2, 4])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("funkcija $sinh(x/2)$ un taas atvasinaajumu")
plt.plot(x,y,"k")
legend.append("$sinh(x/2)$ - dafault- viss ir savienotis ar taisaam liinijaam")
#print(legend)
plt.plot(x,y, "ro")
legend.append("$sin(x/2)$ - tikai dazhi punkti")
#print(legend)

N= len(x)
deltax = x[1] - x[0]
derivative = []

for i in range(N):
    temp=(f(x[i] + deltax)-f(x[i])) / deltax
    derivative.append(temp)

plt.plot(x,derivative,"y")
legend.append("$sin(x/2)$ atvasinaajums - viss ir savienots ar taisnaam liinijaam")
plt.plot(x,derivative,"go")
legend.append("$sin(x/2)$ atvasinaajums - dazhi punkti")


derivative_through_array = []

for i in range (N-1):
    temp = (y[i+1]- y[i]) / (x[i+1]- x[i])
    derivative_through_array.append(temp)

    
plt.plot(x[0:N-1], derivative_through_array,"m")
legend.append("$sins(x/2)$ atvasiinaajums, izmatojot masiiva vertibas")
plt.plot(x[0:N-1], derivative_through_array,"bo")
legend.append("$sins(x/2)$ atvasiinaajums, izmatojot masiiva vertibas")
    
plt.plot(1.200, 0.640, "ch", markersize = 10)

#print(plt.legend._doc_)
#plt.legend(legend, loc="lower left")
plt.legend(legend, loc= 3, fancybox=True, framealpha=0.5, )
plt.show()

