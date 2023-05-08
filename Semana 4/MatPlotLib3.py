import matplotlib.pyplot as plt
import numpy as np

lenguaje=['C','Java','Matlab']
u=[10,30,20]

index=np.arange(len(lenguaje)) #=[0,1,2]

plt.bar(index,u,color='blue')
plt.xlabel('Usuarios')
plt.ylabel('Lenguajes')

plt.xticks(index,lenguaje) #Cambia el nombre del eje x 

plt.show()