"""
Cree un programa que lea el monto de un prestamo
Y el plazo en meses, y muestre al usuario el valor las cuotas mensuales 
pagando un interes fijo del 2.7% mensual
Autor: Jesus Aguilar
Fecha: 25 de octubre 2023
"""
#Definir variables

prestamo = float(input("Ingresa monto del prestamo:"))
numerodepagos = int(input("Ingresa el plazo en meses:"))

#Definir la tasa de interes mensual fija
tasa_interes_mensual = 0.027

#Calcular la cuota mensual
cuota_mensual = prestamo * (tasa_interes_mensual * (1 + tasa_interes_mensual) ** numerodepagos) / ((1 + tasa_interes_mensual) ** numerodepagos - 1)

#Imprimir
print("La cuota mensual del prestamo es: " + str(cuota_mensual))