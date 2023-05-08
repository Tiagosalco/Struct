file=open('Semana 5/myfile.txt','r+')
print('file.name: ', file.name)
print('file.mode: ', file.mode)
file.close()
print('se cerro el archivo? ', file.closed)


## Leer un archivo
file=open('Semana 5/myfile.txt','r')
lines=file.readlines()
for line in lines:
    print(line,end='')
file.close()
print()

## Leer mas facil
file=open('Semana 5/myfile.txt','r')
lines=[line.upper() for line in file]
print(lines)


## Escribir un archivo
f=open('Semana 5/nuevofile.txt','w')
f.write('Holaaa \n')
f.write('Chetasss')
f.close()


## WITH
with open('Semana 5/nuevofile.txt','r') as f:
    lines=f.readlines()
    for line in lines:
        print (line, end='')
        
print('')
        
        
## File imput
print('*******FILE INPUT*********')
import fileinput
with fileinput.input(files=('Semana 5/spam.txt','Semana 5/huevos.txt')) as f:
    line=f.readline()
    print(line)
    print('archivo: ', f.filename)
    
    print('1 linea? ', f.isfirstline())
    print('nro de linea ', f.lineno())
    
    for line in f:
        print(line, end='')
        
        
print()

## Buscar posiciones
print('*************POSICIONES***************')
f=open('Semana 5/text.txt','w')
f.write('abcdefghijklmnopqrstuvwxyz')
f.seek(10,0)
f.write("HELLO")  #Escribe hello en la posicion 10
f.seek(2,0)
f.write('booca')
f.close()

with open('Semana 5/text.txt','r') as f:
    for line in f:
        print(line, end='')


## Renombrar y Borrar
import os
os.rename('Semana 5/text.txt','Semana 5/texto.txt')
os.remove('Semana 5/texto.txt')