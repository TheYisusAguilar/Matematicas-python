"""Cree un programa que lea los tres ángulos internos de un triángulo y muestre si los ángulos corresponden a un
triángulo o no.
Autor: Jesus Aguilar
Fecha: 3 Noviembre 2023"""

#Asignación de los tres angulos internos de un triangulo

ang1 = float(input("Ingrese primer angulo:"))
ang2 = float(input("Ingrese segundo angulo:"))
ang3 = float(input("Ingrese tercer angulo:"))

#Desarrollo de programa
suma_angulos = ang1 + ang2 + ang3
if suma_angulos == 180:
    print("Los angulos corresponden a un triangulo.")
else:
    print("Los angulos no corresponden a un triangulo.")