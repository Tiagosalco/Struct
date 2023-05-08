import numpy as np
import matplotlib.pyplot as plt
##                                      EJERCICIO 1
cero=[]
uno=[]
cinco=[]
for i in range(10):
    cero.append(0)
    uno.append(1)
    cinco.append(5)

a=np.array([cero,uno,cinco])
#print(a)


##                                       EJERCICIO 3
def PrintMat(mat):
    

    for i in range(np.size(mat, axis=0)):
        for j in range(np.size(mat, axis=1)):
            print(mat[i][j],end=' ')
        print('')
        
#PrintMat(np.array([(1,2,3,4),(5,6,7,8),(9,0,1,2)]))


##                                       EJRCICIO 4
a=np.array([(1,2,3),(5,6,7),(0,1,2)])
#print(np.linalg.inv(a))


##                                       EJERCICIO 5
ciudad=['Liverpool','Manchester','Londres','Cardiff']
popu=[100,150,500,80]

index=np.arange(len(ciudad)) #=[0,1,2,3]

plt.scatter(index,popu,color='green')
plt.bar(index,popu,color='blue')
plt.xlabel('Population')
plt.ylabel('City')

plt.xticks(index,ciudad)

#plt.show()
