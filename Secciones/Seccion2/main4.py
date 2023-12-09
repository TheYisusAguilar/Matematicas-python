"""Cree un programa que tome el precio de un producto
e imprima su precio final al consumidor un IVA del 19%
Autor:Jesus Aguilar
Fecha: 25 de octubre 2023
"""
#Definir variables (producto,valor, precio final con iva)
producto = input("Ingresa tu producto:")
valor = float(input("Ingresa el valor del producto:"))
IVA = 0.19

#Calcular precio final con iva
total = valor + (valor * 19/100)
print("Producto:" + str(producto))
print("Valor sin iva:$" + str(valor)) 
print("Total con iva:$" + str(total))