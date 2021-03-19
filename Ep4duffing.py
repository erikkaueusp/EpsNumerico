from numpy import arange
from matplotlib.pyplot import *


V = []
X = []
h = 0.01
def g(t,x,v):
 x2 = x*(1-x**2)/2
 return x2



def runge(v):
 x = -1
 h = 0.01


 for t in arange(0,100+h,h):
  X.append(x)
  V.append(v)
  
  k1y = h*v
  k1v = h*g(t,x,v)
  k2y = h*(v+k1v/2)
  k2v = h*g(t+h/2,x+k1y/2,v+k1v/2)
  k3y = h*(v + k2v/2)
  k3v = h*g(t+h/2,x+k2y/2,v+k2v/2)
  k4y = h*(v + k3v)
  k4v = h*g(t+h,x+k3y,v+k3v)
  x = x + (k1y+2*k2y+2*k3y+k4y)/6
  v = v + (k1v + 2*k2v + 2*k3v + k4v)/6




#runge(0.1)
#plot(X,V,color = 'red',label = '0.1')
#X,V = [],[]
runge(0.5)
plot(X,arange(0,100+h,h),color = 'green',label = '0.5')

#runge(1)
#plot(X,V,color = 'blue',label = '1')
legend(loc = 'upper right')
title(r"Runge-Kutta 4 ($x'' = \frac{x(1-x^2)}{2}$)")
ylabel('v - velocidade')
xlabel('x - posição')
show()
