from numpy import pi, cos, arange,empty
from scipy.integrate import odeint
from matplotlib.pyplot import *
from numba import jit

@jit(nopython=True)
def pend(y0,t,gama2,F):
 x,v = y0 
 dvdt = [v,x*(1-x**2)/2 - gama2*v + F*cos(t)]
 return dvdt





df = 0.0005
for F in arange(0,0.7+df,df):
 T = []
 TIME = []
 h = 0.02*pi
 t = 0
 for i in range(1,200):
  t = t + h
  T.append(t)

 X = odeint(pend,[-1,1],T,args=(0.25,F))
 h = 0.002*pi
 for i in range(1,10):
  for j in range(1,10):
   t = t + h
   TIME.append(t)
  X = odeint(pend,[X[len(T)-1,0],X[len(T)-1,1]],TIME,args=(0.25,F))
  scatter(X[len(TIME)-1,0],X[len(TIME)-1,1],color = 'black',s=1)
  T = TIME
  TIME = []






title("Diagrama de Bifurcação")
ylabel('X')
xlabel('Força')
show()