"""Cree un programa que lea la edad
de un usuario y muestre cuántos años
tendra el usuario dentro de tantos 
años como el usuario indique
Autor: Jesus Aguilar
Fecha: 20 de Octubre 2023
"""
#En esta parte el usuario va a ingresar su edad
edad = input("Por favor, ingresa tu edad: ")
numero1 = int(edad)

#En esta parte se toma en cuenta la edad que desea considerar el usuario
anios_adicionales = input("¿Cuantos años mas te gustaria considerar?: ")
numero2 = int(anios_adicionales)
 
#En esta parte se calcula la edad, con la edad que desea considerar el usuario
edadproyectada= numero1 + numero2

#Edad que tendra segun indique el usuario

print("Esta es tu edad según los años que indicaste: " + str(edadproyectada))

