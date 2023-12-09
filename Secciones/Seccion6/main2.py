"""Cree un programa que calcula la suma de los primeros n números naturales.
Autor: Jesus Aguilar"""

# Calcula la suma de los primeros n números naturales

n = int(input("Ingrese un número: "))

suma = 0
i = 1
while i <= n:
    suma += i
    i += 1

print("La suma de los primeros", n, "números naturales es", suma)
