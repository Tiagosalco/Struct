import os

try:
    fichero=open('SSSSSSSSSSSSSSSSSemana 5/huevos.txt')
    for linea in fichero:
        print(linea,end='')
        
    fichero.close()
    
except IOError:
    print('el archivo no existe')
    

try:
    print(8/2)
except ZeroDivisionError as e:
    print(e)
else: #solo se ejecuta si hubo una excepcion
    print('todo bien')
finally: #Siempre se ejecuta
    print('xdxd')