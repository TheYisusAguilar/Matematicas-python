"""Cree un programa que calcule el promedio de tres notas para n estudiantes.
Autor: Jesus Aguilar
Fecha: 3 Noviembre 2023"""

# Solicitar al usuario que ingrese el número de estudiantes
n = int(input("Ingrese el número de estudiantes: "))

# Inicializar una lista para almacenar los promedios
promedios = []

# Calcular el promedio de notas para cada estudiante
for i in range(n):
    print(f"Notas del estudiante {i + 1}:")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    promedio = (nota1 + nota2 + nota3) / 3
    promedios.append(promedio)

# Imprimir los promedios de los estudiantes
for i, promedio in enumerate(promedios, start=1):
    print(f"El promedio del estudiante {i} es: {promedio:.2f}")
