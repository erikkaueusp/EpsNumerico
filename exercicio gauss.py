import numpy as np #biblioteca usada para importar um array ou vetor.

M = np.array([[0,5,-1,5],[11,0,1,14],[1,-1,-1,0]],float)  #Matriz aumentada.
n = len(M) # pega o número de linhas da matriz, nesse caso n = 3.
print("Nossa Matriz aumentada é : \n",M)

#Pivotamento parcial, no qual verifica o maior valor da coluna inicial e substitui pela respectiva linha que possui o valor.
indice = np.argmax(M[0:n,0]) # retorna o indice do valor máximo da primeira coluna.
if indice != 0 :
 aux = np.copy(M[0])
 M[0] = M[indice]
 M[indice] = aux
 print("\n Troca de linha: \n",M)


#triangularização da matriz.

for i in range (1,n):
 p = M[i-1,i-1]  # pivo inicial.
 if p != 0.0:
 
  for j in range (i,n):
   m = M[j,i-1]/p   #coeficiente que multiplica a linha do pivo.
   M[j] = M[j] -m*M[i-1]  # metodo de gauss.
   print("\n Eliminação de Gauss: \n",M)
   
 else:  #caso o pivo da segunda linha seja 0, esta linha é copiada e acaba sendo trocada pela ultima linha e a ultima recebe esta.
  aux = np.copy(M[i-1])
  M[i-1] = M[i]
  M[i] = aux
  print(M)
  
#substituição para encontrar os valores de x0,x1,x2,x3..xn
 
z = float(M[i,j+1]/M[i,j])
resultado = np.zeros(n)
resultado[n-1] = z
for i in range(n-2,-1,-1):
 resultado[i] = (M[i,j+1] - np.dot(resultado,M[i,0:n]))/M[i,i]
print("\nO resultado de x0,x1,x2... é o vetor: \n ",resultado)
 