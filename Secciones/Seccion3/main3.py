"""Cree un programa que reciba dos numeros y muestre el mayor
En caso que los dos numeros sean iguales se debe mostrar al usuario
Autor:Jesus Aguilar
Fecha: 25 Octubre 2023
"""

#Aqui se van a ingresar los dos numeros
num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingrese segundo número: "))

#Afirmar si el numero es mayor o menor y si estos son iguales aqui.

if num1 > num2:
    print(f"{num1} Es mayor que {num2}.")
elif num2 > num1:
    print(f"{num2} Es mayor que {num1}.")
else:
    print(f"Ambos números, {num1} y {num2}, son iguales.")