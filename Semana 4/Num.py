import numpy as np


a=np.array([1,2,3])
#print(a)

b=np.array([(10,20,30),(11,22,33)])
#print(b)

c=np.ones(2)
#print(c)

## Vector de a dos en dos de 1 a 9 sin incluir el 9
d=np.arange(1,9,2)
#print(d)

e=np.array([1,4,62,26,72,99])
#print(np.sort(e))

f=np.array([1,2,4])
g=np.array([3,5,6])
#print(np.concatenate((f,g)))


# Matriz 3D
mat=np.array(
    [[[1,2,3],[4,5,6]],
     [[11,22,33],[10,20,30]],
     [[13,23,34],[17,27,37]]
     ]
)
#print(mat.ndim) #Dimensionws
#print(mat.shape) #Ancho largo alto
#print(size(mat))# Cantidad de elementos

h=np.arange(6)
#print(h.reshape(2,3))

i=np.array([[1,2,3],[11,12,8],[31,32,3]])
#print(i.max(axis=0)) #imprime los 3 maximos
#print(i.max(axis=1)) #imprime los maximos de cada fila

j=np.arange(6).reshape(2,3)
for x in np.nditer(j):
    print(x, end=' ')
