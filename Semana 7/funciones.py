
def saludo(nombre,mensaje='larga vida y prosperidad'): #LE PUSE UN VALOR DE DEFAULT
    print('bienvenido', nombre,',',mensaje)
    
saludo('gerardo')
saludo('gerardo','un gusto')
saludo(mensaje='buenas buenas',nombre='gerardo')

def saludos(*args): #  *
    for nombre in args:
        print('hola',nombre)
    
saludos('juan','mica','delfi')

def mostrar(**kwargs): #  **
    for key in kwargs.keys():
        print('argumento',key,'tiene valor de ', kwargs[key])
    
mostrar(nombre='mica',apellido='rosa',edad='18')