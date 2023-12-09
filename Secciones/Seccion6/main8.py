"""Cree un programa que calcule la suma de los cuadrados de los números entre 1 y n
Autor:Jesus Aguilar"""

# Calcula la suma de los cuadrados de los números entre 1 y n

n = int(input("Ingrese un número: "))

suma = 0
i = 1

while i <= n:
    suma += i ** 2
    i += 1

print("La suma es", suma)
