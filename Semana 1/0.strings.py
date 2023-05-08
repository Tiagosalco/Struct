#print('hola mundo')
#print("hola a \'todes\'mundo2") #es lo mismo una o dos comillas pero no mezclar
#si quiero que aparezca la comilla antes poner /

dato1="buenas noches"
dato2=' como estan'

#print(dato1 + dato2)

#print(dato1[0:3])

#split	separar		VARIABLE.split(, o ' ')		separar de a cuerdo donde haya espacios o coma o lo que sea y lo borra del nuevo variable	
#count	contar caracteres		Variable.count(, o " ")			contar la cantidad e espacios o comas que haya 

# Encontrar FIND

a=dato1.find('noches') #Encuentra la palabra noches en el dato
#print(a)

#fprintf con %d y %s de matlab
nombre='tiago'
print('nombre completo: {} {}'.format(nombre,'salcovich'))

#alineacion
print('-> {:<25} <-'.format('alineado izq')) 
print('-> {:^30} <-'.format('alineado centro'))
print('-> {:>35} <-'.format('alineado der'))
#entre {} va en la cantiad de espacios que hay que alinear
# para numeros pones {:,} y hae comas cada 3 numeros para leer mejor 

apellido=input('Ingrese su apellido: ')

