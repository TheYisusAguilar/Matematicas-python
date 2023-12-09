"""Cree un programa que dado un número entero n, calcule su factorial(n!).
Autor: Jesus Aguilar
Fecha: 3 Noviembre 2023
"""

# Definir una función para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es negativo
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}.")
