from numpy import arange,cos,pi
from matplotlib.pyplot import *
from numba import jit

V = []
X = []
time = 0
@jit(nopython=True)
def g(t,x,v,F):
 x2 = x*(1-x**2)/2 -0.25*v + F*cos(t)
 return x2


def runge(v,F):
 x = -1
 h = 0.01*2*pi

 for t in arange(0,200000+h,h):
  
  k1y = h*v
  k1v = h*g(t,x,v,F)
  k2y = h*(v+k1v/2)
  k2v = h*g(t+h/2,x+k1y/2,v+k1v/2,F)
  k3y = h*(v + k2v/2)
  k3v = h*g(t+h/2,x+k2y/2,v+k2v/2,F)
  k4y = h*(v + k3v)
  k4v = h*g(t+h,x+k3y,v+k3v,F)
  x = x + (k1y+2*k2y+2*k3y+k4y)/6
  v = v + (k1v + 2*k2v + 2*k3v + k4v)/6
  time = t
 h = 0.001*2*pi
 for i in range(20000):
  for j in range(1000):
   k1y = h*v
   k1v = h*g(time,x,v,F)
   k2y = h*(v+k1v/2)
   k2v = h*g(time+h/2,x+k1y/2,v+k1v/2,F)
   k3y = h*(v + k2v/2)
   k3v = h*g(time+h/2,x+k2y/2,v+k2v/2,F)
   k4y = h*(v + k3v)
   k4v = h*g(time+h,x+k3y,v+k3v,F)
   x = x + (k1y+2*k2y+2*k3y+k4y)/6
   v = v + (k1v + 2*k2v + 2*k3v + k4v)/6
   time = time + h
  print(v)
  X.append(x)
  V.append(v)


runge(1,0.28)


scatter(X,V,color='red',s=1)
title("Mapa de Poincaré")
ylabel('V[m/s]')
xlabel('X[m]')
show()
