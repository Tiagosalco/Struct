import csv

notas = []
cursos = [[], [], [], []]

with open('MATE IV 93.65.csv') as file:
    reader = csv.reader(file)
    next(reader)  # saltar la primera fila
    for row in reader:
        try:
            nota = float(row[5])
            notas.append(nota)
            curso = row[1][0]  # obtener la primera letra del curso
            if curso == 'A':
                cursos[0].append(nota)
            elif curso == 'B':
                cursos[1].append(nota)
            elif curso == 'C':
                cursos[2].append(nota)
            elif curso == 'D':
                cursos[3].append(nota)
        except ValueError:
            continue  # saltar esta fila si no se puede convertir a float

# calcular promedios y cantidad de aprobados por curso
for i in range(4):
    curso = cursos[i]
    num_estudiantes = len(curso)
    num_aprobados = sum(1 for nota in curso if nota >= 4)
    promedio = sum(curso) / num_estudiantes if num_estudiantes > 0 else 0
    print(f"Del curso {chr(65+i)} aprobaron {num_aprobados} y el promedio fue de {promedio:.2f}")

# calcular cantidad de aprobados y promedio general
num_aprobados = sum(1 for nota in notas if nota >= 4)
promedio_general = sum(notas) / len(notas) if len(notas) > 0 else 0
print(f"Aprobaron {num_aprobados} en total y el promedio general fue de {promedio_general:.2f}")

print('\nAhora contando los ausentes:')

with open('MATE IV 93.65.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Saltea la primera línea (cabecera)
    next(reader)
    
    # Inicializa listas y variables
    cursos = [[], [], [], []]
    notas = []
    
    # Lee cada fila del archivo CSV
    for row in reader:
        # Intenta convertir la nota a float, si falla asigna 0
        try:
            nota = float(row[5])
        except ValueError:
            nota = 0.0
        
        # Agrega la nota a la lista
        notas.append(nota)
        
        # Clasifica la nota según el curso
        if row[1] == 'A':
            cursos[0].append(nota)
        elif row[1] == 'B':
            cursos[1].append(nota)
        elif row[1] == 'C':
            cursos[2].append(nota)
        elif row[1] == 'D':
            cursos[3].append(nota)

# Filtra las notas distintas de 0
notas = list(filter(lambda nota: nota != 0, notas))

# Inicializa variables para el promedio
promedios = []
aprobados = []

# Calcula el promedio y la cantidad de aprobados de cada curso
for curso in cursos:
    aprobados.append(sum(1 for nota in curso if nota >= 4))
    promedio = sum(curso) / len(curso) if curso else 0.0
    promedios.append(promedio)

# Imprime los resultados
for i in range(len(cursos)):
    print(f"Del {i+1} aprobaron {aprobados[i]} y el promedio fue de {promedios[i]:.2f}")
print(f"Aprobaron {sum(1 for nota in notas if nota >= 4)} en total y el promedio total fue de {sum(notas)/110:.2f}")
