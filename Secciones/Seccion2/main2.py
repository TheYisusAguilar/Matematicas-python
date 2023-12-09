"""Cree un programa que tome el radio
de un circulo e imprima su area y perimetro
Autor: Jesus Aguilar
Fecha: 25 de octubre 2023
"""
#Definir variables (radio, area y perimetro)
import math
circulo = float(input("Circunferencia: "))
radio = circulo / (2 * math.pi)

#Calcular area de un circulo
area = math.pi * radio ** 2

#Calcular el perimetro de un circulo
perimetro = 2 * math.pi * radio
print("Area del circulo:" + str(area))
print("Perimetro del circulo:" + str(perimetro))