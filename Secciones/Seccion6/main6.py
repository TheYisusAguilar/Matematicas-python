"""Cree un programa que calcule el promedio de 10 números
Autor:Jesus Aguilar
"""

# Calcula el promedio de 10 números

i = 1
suma = 0
while i <= 10:
    numero = float(input("Ingrese un número: "))
    suma += numero
    i += 1

promedio = suma / 10

print("El promedio es", promedio)
