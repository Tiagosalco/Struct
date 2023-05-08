import datetime
import random
from pathlib import Path as path
import csv

                            ############### EJERCICIO 1 ###############
# Creo el nombre
#a=input('Ingrese nombre del archivo: ')
a='ej1'
nombre=('Guias/Guia7/{0}.txt'.format(a))
#Creo el archivo
f=open(nombre,'w')

fecha=datetime.datetime.today()
fecha=str(fecha.date())
f.write(fecha)
f.close()

                            ############### EJERCICIO 2 ###############
                            
ff=open('Guias/Guia7/numbers.txt','w') 
numeros=[random.randint(1, 100) for i in range(5)]
numeros=",".join(str(n) for n in numeros) #Crea un string de los numeros separados por una coma

ff.write(numeros)

p=path.cwd()
print('El directorio es {0}'.format(p))

ff.close()


                            ############### EJERCICIO 3 ###############
opciones = [
    "1. Opción 1",
    "2. Opción 2",
    "3. Opción 3",
    "4. Salir"
]
print("Menú:")
for opcion in opciones:
    print(opcion)
#opcion = input("Elija una opción: ")


opcion='4'

if opcion=='1':
    #op=input('Ingrese nombre del archivo que quiere crear y formato: ')
    op='ej3.txt'
    nombre=('Guias/Guia7/{0}'.format(op))
    fff=open(nombre,'w') 
elif opcion=='2':
    #op=input('Ingrese nombre del archivo a leer y formato: ')
    op='ej3.txt'
    nom=('Guias/Guia7/{0}'.format(op))
    fff=open(nom,'r')
    lines=fff.readlines()
    for line in lines:
        print(line,end='')
elif opcion=='3':
    #op=input('Ingrese nombre del archivo a agregar informacion: ')
    op='ej3.txt'
    nom=('Guias/Guia7/{0}'.format(op))
    fff=open(nom,'a')
    agregar=input('Informacion a agregar: ')
    fff.write(agregar)
elif opcion=='4':
    print('Hasta luego')

                            ############### EJERCICIO 4 ###############
                            
with open('./Guias/Guia7/ej4.csv','w', newline='') as csvfile:
    fieldnames=['Tipo','Transaccion','Importe']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {
            'Tipo': 'ahorros',
            'Transaccion': 'deposito',
            'Importe': random.randint(100, 1000)
        }
    )
    writer.writerow(
        {
            'Tipo': 'corriente',
            'Transaccion': 'extraccion',
            'Importe': random.randint(100, 1000)
        }
    )
    writer.writerow(
        {
            'Tipo': 'inversion',
            'Transaccion': 'deposito',
            'Importe': random.randint(100, 1000)
        }
    )    
    
print(  )    
                           ############### EJERCICIO 5 ###############
                           
with open('Guias/Guia7/libros.csv','w', newline='') as csvfile:
    fieldnames=['Book','Author','Year Released']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {
            'Book': 'Mockingbird',
            'Author': 'Harper',
            'Year Released': 1960
        }
    )
    writer.writerow(
        {
            'Book': 'Time',
            'Author': 'Hawking',
            'Year Released': 1988
        }
    )
    writer.writerow(
        {
            'Book': 'Gatsby',
            'Author': 'Fitzgerald',
            'Year Released': 1922
        }
    )
    writer.writerow(
        {
            'Book': 'Hat',
            'Author': 'Sacks',
            'Year Released': 1985
        }
    )
    writer.writerow(
        {
            'Book': 'Pride',
            'Author': 'Austen',
            'Year Released': 1813
        }
    )




with open('Guias/Guia7/libros.csv','a', newline='') as csvfile:
    fieldnames=['Book','Author','Year Released']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    
    agregar=input('Ingrese cantidad de filas para agregar: ')
    for i in range(int(agregar)):
        writer.writerow(
            {
                'Book': str(input('ingrese libro: ')),
                'Author': str(input('ingrese Autor: ')),
                'Year Released': int(input('ingrese ano de publicacion: '))
            }
        )
        

with open('Guias/Guia7/libros.csv', newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading,end='\t\t')
    print('\n---------------\n')
    for row in reader:
        if 1900<int(row['Year Released'])<2000:
            print(row['Book'],row['Author'],row['Year Released'],sep='\t\t')

