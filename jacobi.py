import numpy as np

A = np.array([[11,0,1],[0,5,-1],[1,-1,-1]],float) # matriz A dos coeficientes
b = np.array([[14,5,0]],float) # matriz coluna b 
n = len(A) #pega o indice n da matriz nxn
x = np.zeros(n) # vetor chute inicial, (0,0,0...) = (x1,x2,x3...)
aux = np.zeros(n) # vetor que vai receber os novos valores da equação com o chute inicial 
t = 0 # inicia em 0 e vai até n quando todos os valores do vetor são menores que o erro dado, nesse exemplo 10^-3
a = 1 # contador das iterações do método
print("iteração n = ",a)
for i in range(0,n): # primeiro calculo
 aux[i] = (1/A[i,i])*(b[0,i] - np.dot(A[i],x) + A[i,i]*x[i])
 print("Valores de x(k-1): ",x)
 print("Valores de x(k): ",aux)
 print("Valor do erro x%.d: "%(i+1),abs(x[i]-aux[i]))

while t != n :
 x = np.copy(aux) # copia o novo valor para o vetor x que era os chutes anteriores
 
 print("Valor x(k-1) : ",x)
 a = a + 1
 print("\n iteração n = ",a)
 for i in range(0,n):
  aux[i] = (1/A[i,i])*(b[0,i] - np.dot(A[i],x) + A[i,i]*x[i])
 print("Valor x(k) : ",aux)
 for k in range (0,n):
  print("Valor do erro x%.d: "%(k+1),abs(x[k]-aux[k]))
 
  if abs(x[k] - aux[k]) < 10**(-3) :
   t = t + 1 # quando todos os valores da diferença dos vetores são menores que o erro, o valor de t se torna o número de elementos desse vetor.
  else:
   t = 0
   
