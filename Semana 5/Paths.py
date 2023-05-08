from pathlib import Path as path
# Crear path en el directorio actuak

p=path('.')
print(p)
print(p.exists())
print(p.is_dir())
print(p.is_file())
print(p.is_absolute())

p=path.cwd()
print('El directorio es {0}'.format(p))
print('\n')

newdir= p/'test'
newdir.mkdir()#ahora existe el directorio
