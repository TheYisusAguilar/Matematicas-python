"""Cree un programa que lea la edad de un usuario e imprima
un mensaje que diga si el usuario es mayor de edad o no
Autor:Jesus Aguilar
Fecha:25 Octubre 2023
"""
#Definir variables (edad)
edad = int(input("Ingresa tu edad:"))

if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")