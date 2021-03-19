from numpy import arange,sqrt,pi,sin,cos
import matplotlib.pyplot as plt


Tgal = 2*pi*sqrt(1/9.8)
 
 
def trapezio(a,b,n,theta):
 def function(x,theta):
  l = 1
  g = 9.8
  k = (1-cos(theta))/2
  y = 4*sqrt(l/g)*(1/sqrt(1-k**2*(sin(x)**2)))
  return y
 
 X,Y,I, = [],[],[]
 h = (b-a)/n
 for i in arange(a,b+h,h):
  X.append(i)
  Y.append(function(i,theta),)
 for j in range(1,len(Y)-1):
  I.append(Y[j])
  
 I.append((Y[0] + Y[j+1])/2)
 soma = (sum(I)*(h))
 X,Y,I, = [],[],[]
 return soma
 
print("Valores de theta [0;pi)    |     Valor de T")
print("-"*50)
for theta in arange(0,pi,pi/20):
 print(f'{theta:<25}'," | ",f'{trapezio(0,pi/2,10000,theta):<20}')
 plt.plot(theta,trapezio(0,pi/2,10000,theta),'rs')
 
plt.xlabel("Valores de theta")
plt.ylabel("T/Tgalileu")
plt.show()
 