lista=[]
n=5

for i in range(0,n):
    x=input('Ingrese Palabras o Numeros: ')
    lista.append(x)
    
print(lista)
for i in reversed(lista):
    print(i)
        