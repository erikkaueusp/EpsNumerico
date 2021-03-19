def g(t,y1,z):
 y3 =  z - y1 + t**3 - 3*t**2 + 6*t # Edo a ser resolvida
 return y3

def euler(): # função para o método de Euler com os valores iniciais onde h = 0.01 repetindo 600 vezes até t = 6 segundos
 z = 0
 y1 = 0
 n = 600
 h = 0.01
 for i in range(n+1):
  t = h*i
  y1 = y1 + h*z
  z = z + h*g(t,y1,z)
 return y1,z

def runge(): #função para o método de Runge-Kutta 4ª ordem para os mesmos valores até t = 6s
 z = 0
 y1 = 0
 n = 600
 h = 0.01
 for i in range(n+1):
  t = h*i
  k1y = h*z
  k1z = h*g(t,y1,z)
  k2y = h*(z+k1z/2)
  k2z = h*g(t+h/2,y1+k1y/2,z+k1z/2)
  k3y = h*(z + k2z/2)
  k3z = h*g(t+h/2,y1+k2y/2,z+k2z/2)
  k4y = h*(z + k3z)
  k4z = h*g(t+h,y1+k3y,z+k3z)
  y1 = y1 + (k1y+2*k2y+2*k3y+k4y)/6
  z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
 return y1,z

print("Método de Euler para y e z respectivamente",euler())
print("\nMétodo de Runge para y e z respectivamente",runge())