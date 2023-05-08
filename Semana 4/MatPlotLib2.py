import matplotlib.pyplot as plt

x=[-10,-8,-3,-1,0,1,5,6,9]
y=[]

n=0
for i in range(len(x)):
    y.append(max(n,x[i])) # a las posiciones que sean menores que N, les asigna N
    
print(y)
    
plt.plot(x,y)

plt.title(label='prueba',
          fontsize=40,
          color='red')
plt.show()