"""
Cree un programa que lea dos números
Y muestre su producto, su cociente, su modulo, su suma y su resta
Autor: Jesus Aguilar
Fecha: 25 octubre 2023
"""
option = (input("Ingrese una opción || opcion 1 - para calcular el producto, opcion 2 - para cociente, opcion 3  - para modulo, opcion 4 - para suma, opcion 5 - para resta: "))
num1 = int(input("Ingrese primer número:"))
num2 = int(input("Ingrese segundo número:"))
operacion = int

#Calcular el producto de dos números
if option == "1":
    operacion = num1 * num2

if option == "2":
    operacion = num1 / num2
    
if option == "3":
    operacion = num1 % num2
    
if option == "4":
    operacion = num1 + num2
    
if option == "5":
    operacion = num1 - num2
    
print("Resultado:" + str(operacion))
    