"""Cree un programa que muestre los números impares entre 1 y n
Autor:Jesus Aguilar"""

# Muestra los números impares entre 1 y n

n = int(input("Ingrese un número: "))

i = 1
while i <= n:
    if i % 2 == 1:
        print(i)
    i += 1
