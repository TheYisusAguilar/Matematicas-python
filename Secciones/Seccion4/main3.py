"""Cree un programa que lea un número y muestre si éste es divisible entre cinco o no.
Autor: Jesus Aguilar
Fecha: 3 Noviembre 2023"""

#Aqui el usuario ingresa el numero

numero = int(input("Ingresa número:"))

 #Verificar si el numero es divisible o no entre cinco.
 
if numero % 5  == 0:
     print(f"El número {numero} es divisible entre cinco.")
else:
     print(f"El número {numero} no es divisible entre cinco.")