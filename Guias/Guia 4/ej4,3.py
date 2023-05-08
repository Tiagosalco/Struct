importe=int(input('Ingrese importe a evaluar: '))
billetes=[1000,500,200,100,50,20,10,5,2,1]
cantidad_billetes=[]

for billete in billetes:
     cantidad=importe // billete
     cantidad_billetes.append(cantidad)
     importe%=billete
        
for i in range(len(billetes)):
     if cantidad_billetes[i]>0:
         print('{0} billete(s) de {1}'.format(cantidad_billetes[i],billetes[i]))
            
            
        
