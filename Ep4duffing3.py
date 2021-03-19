from numpy import arange,cos
from matplotlib.pyplot import *


V = []
X = []
def g(t,x,v,a,F):
 x2 = x*(1-x**2)/2 -a*v + F*cos(t)
 return x2



def runge(v,a,F):
 x = -1
 h = 0.01
 #X.append(x)
 #V.append(v)
 for t in arange(0,4000+h,h):
  
  k1y = h*v
  k1v = h*g(t,x,v,a,F)
  k2y = h*(v+k1v/2)
  k2v = h*g(t+h/2,x+k1y/2,v+k1v/2,a,F)
  k3y = h*(v + k2v/2)
  k3v = h*g(t+h/2,x+k2y/2,v+k2v/2,a,F)
  k4y = h*(v + k3v)
  k4v = h*g(t+h,x+k3y,v+k3v,a,F)
  x = x + (k1y+2*k2y+2*k3y+k4y)/6
  v = v + (k1v + 2*k2v + 2*k3v + k4v)/6
  if t>2000:
   X.append(x)
   V.append(v)



runge(1,0.25,0.23)
plot(X,V,color = 'red',label = '0.6')
X,V = [],[]
#runge(1,0.25,0.23)
#plot(X,V,color = 'green',label = '0.23')
#X,V = [],[]
#runge(1,0.25,0.28)
#plot(X,V,color = 'blue',label = '0.28')
#X,V = [],[]
#runge(1,0.25,0.35)
#plot(X,V,color = 'orange',label = '0.35')
#X,V = [],[]
#runge(1,0.25,0.6)
#plot(X,V,color = 'purple',label = '0.6')
legend(loc = 'upper right')
title("Espaço de fase")
ylabel('v - velocidade')
xlabel('x - posição')
show()
