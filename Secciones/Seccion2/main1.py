"""Cree un programa que tome la base y la altura de un triangulo
e imprima su area
Autor: Jesus Aguilar
Fecha: 25 de Octubre
"""
#Definir variables (base,altura y area)
base = float(input("Ingresa la base del triangulo:"))
altura = float(input("Ingresa la altura del triangulo:"))

#Calcular el area
area = (base * altura) / 2

#Imprimir area
print("El area de un triangulo es:" + str(area))