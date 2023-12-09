"""Cree un programa que imprima los números enteros entre 0 y 100 en orden ascendente y descendente.
Autor: Jesus Aguilar
Fecha: 3 Noviembre 2023"""

# Imprimir los números en orden ascendente
print("Números en orden ascendente:")
for i in range(101):
    print(i, end=" ")

# Salto de línea
print("\n")

# Imprimir los números en orden descendente
print("Números en orden descendente:")
for i in range(100, -1, -1):
    print(i, end=" ")
