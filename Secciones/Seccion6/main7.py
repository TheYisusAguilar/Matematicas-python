"""Cree un programa que muestre el promedio de n números, dejándose de solicitar números cuando se
introduzca el cero.
Autor: Jesus Aguilar"""

# Muestra el promedio de n números

suma = 0
contador = 0

numero = float(input("Ingrese un número: "))

while numero != 0:
    suma += numero
    contador += 1
    numero = float(input("Ingrese un número: "))

promedio = suma / contador

print("El promedio es", promedio)
