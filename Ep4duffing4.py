from numpy import arange,cos,pi
from matplotlib.pyplot import *
from numba import jit

V = []
X = []
forca = []

@jit(nopython=True)
def g(t,x,v,F):
 x2 = x*(1-x**2)/2 -0.25*v + F*cos(t)
 return x2


def runge(v,F):
 x = -1
 h = 0.01*2*pi
 t = 0
 for i in range(200000):
  
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
  t = t + h
 h = 0.001*2*pi
 for i in range(100):
  for j in range(1000):
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
   t = t + h
  X.append(x)
  forca.append(F)

df = 0.0005
for f in arange(0,0.7+df,df):
 runge(1,f)


scatter(forca,X,color='black',s=1)
title("Diagrama de Bifurcação")
ylabel('X')
xlabel('Força')
show()
