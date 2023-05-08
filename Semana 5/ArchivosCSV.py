import csv

with open('./Semana 5/sample.csv','w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['Ella es una chica', 'real'])
    writer.writerow(['Hermosa','fatal'])
    writer.writerow(['Que nos','enamora'])
    
print()

with open('./Semana 5/sample.csv', newline='') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        #print(*row,sep=' -- ') # -- que poner entre cada 'celda'
        print('*')
print('**')

# Con nombres de columnas
with open('./Semana 5/nombres.csv','w', newline='') as csvfile:
    fieldnames=['Nombre','Apellido','Resultado']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {
            'Nombre': 'Agus',
            'Apellido': 'Perez',
            'Resultado': 54
        }
    )
    writer.writerow(
        {
            'Nombre': 'Delfi',
            'Apellido': 'Rudy',
            'Resultado': 69
        }
    )
    writer.writerow(
        {
            'Nombre': 'Jaz',
            'Apellido': 'Swarc',
            'Resultado': 99
        }
    )    
    writer.writerow(
        {
            'Nombre': 'Britta',
            'Apellido': 'nsnkkk',
            'Resultado': 40
        }
    )

with open('./Semana 5/nombres.csv', newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading,end='\t\t')
    print('\n---------------\n')
    for row in reader:
        print(row['Nombre'],row['Apellido'],row['Resultado'],sep='\t\t')
