"""Cree un programa que lea una cantidad
e imprima un porcentaje a calcular requerido sobre esa cantidad
Autor: Jesus Aguilar
Fecha: 25 Octubre 2023
"""
#Definir variables (cantidad,porcentaje)
cantidad = int(input("Ingresa la cantidad:"))
porcentaje = float(input("Ingresa el porcentaje:"))

resultado = (cantidad * porcentaje)/100
print("Resultado:" + str(resultado))