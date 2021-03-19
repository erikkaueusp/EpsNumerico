from numpy import sqrt


def lcg(z):
 m = 2147483647
 a = 16807
 z = (a*z) % m
 return z, z/m
z = 8516455
X = []
Y = []
n = 0
m = 100
I = []
variancia = 0
print("-----N tentativas-----|--------Im--------|-------Sigma-------|-----Sigma(medio)----- ")
for p in range(1,18):
 for N in range(1,2**p+1):
  for i in range(m):
   z,x = lcg(z)
   X.append(x)
   z,y =lcg(z)
   Y.append(y)
   if X[i]**2 + Y[i]**2 <= 1:
    n += 1
   integral = 4*n/m
  I.append(integral)
  X = []
  Y = []
  n = 0
 Imedio = sum(I)/N
 for i in range(N):
  variancia += ((I[i] - Imedio)**2)/(N-1)
 sigma = sqrt(variancia)
 variancia = 0
 I = []
  
 print(f'{N:>10}',f'{Imedio:>30}',f'{sigma:>18}',f'{sigma/sqrt(N):>19}')
 


