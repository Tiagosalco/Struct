
a=[1,2,3,4,5]
#for x in reversed(a):
 #   print(x)
    
#for i in range(1,6) :
  #  print('hola')

cant=0
while cant<10:
    print(cant,' ', end='') #Con este end= hago que sea en la misma linea
    cant+=1
    
for nombre in ['pepe','ana','juan']:
    print('hola, {0} todo bien?'.format(nombre))
    
    
num=2
for potencia in [2,3,4,5]:
    print('{0} elevado a la {1} es {2}'.format(num,potencia,num**potencia)) 
    
    
s=('11dffdc')
for i in range(len(s)):
    print(s[i])
    