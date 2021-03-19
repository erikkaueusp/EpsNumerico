from numpy import arange
from matplotlib.pyplot import *


V = []
X = []
def g(t,x,v,a):
 x2 = x*(1-x**2)/2 -a*v
 return x2



def runge(v,a):
 x = -1
 h = 0.1
 X.append(x)
 V.append(v)
 for t in arange(0,30+h,h):
  
  k1y = h*v
  k1v = h*g(t,x,v,a)
  k2y = h*(v+k1v/2)
  k2v = h*g(t+h/2,x+k1y/2,v+k1v/2,a)
  k3y = h*(v + k2v/2)
  k3v = h*g(t+h/2,x+k2y/2,v+k2v/2,a)
  k4y = h*(v + k3v)
  k4v = h*g(t+h,x+k3y,v+k3v,a)
  x = x + (k1y+2*k2y+2*k3y+k4y)/6
  v = v + (k1v + 2*k2v + 2*k3v + k4v)/6
  X.append(x)
  V.append(v)



runge(1,0.25)
plot(X,V,color = 'red',label = '2$\gamma = 0.25$')
X,V = [],[]
runge(1,0.8)
plot(X,V,color = 'green',label = '2$\gamma = 0.8$')

legend(loc = 'upper right')
title("Espaço de fase")
ylabel('v - velocidade')
xlabel('x - posição')
show()
