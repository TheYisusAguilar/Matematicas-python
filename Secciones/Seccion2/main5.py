"""Cree un programa que tome el valor de un producto e imprima 
su precio final si este tiene siempre un descuento del 10%
Autor:Jesus Aguilar
Fecha:25 Octubre 2023
"""

#Definir variables (Producto,valor, total final con descuento del 10%)
producto = input("Ingresa tu producto:")
valor = float(input("Ingresa el valor de tu producto:"))
Descuento = 0.10

#Calcular valor del producto con el descuento del 10%
totalfinal = valor - (valor * 10/100)
print("Producto:" + str(producto))
print("Valor de tu producto:$" + str(valor))
print("Total con descuento del 10%:$" + str(totalfinal))