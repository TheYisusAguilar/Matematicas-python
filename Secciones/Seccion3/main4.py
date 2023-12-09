"""Cree un programa que reciba tres números y muestre el mayor.
En caso de que los tres números sean iguales tambien
Se debe mostrar al usuario
Autor:Jesus Aguilar
Fecha: 25 de Octubre"""

#Aqui el usuario asigna los números

num1 = float(input("Ingresa primer número:"))
num2 = float(input("Ingresa segundo número:"))
num3 = float(input("Ingresa tercer número:"))

#Aqui se desarrolla el programa

if num1 == num2 == num3:
    print(f"Todos los números, {num1}, {num2} y {num3}, son iguales")
else:
    mayor = max(num1,num2,num3)
    print(f"El número mayor es {mayor}.")