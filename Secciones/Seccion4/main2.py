"""Cree un programa que lea un número y muestre si éste es par o impar.
Autor: Jesus Aguilar
Fecha: 3 Noviembre 2023"""

#Aqui el usuario ingresa el número:

numero = int(input("Ingresa número:"))

#Verificar si es par o impar

if numero % 2 == 0:
    print(f"El numero {numero} es par.")
else:
    print(f"El numero {numero} es impar.")