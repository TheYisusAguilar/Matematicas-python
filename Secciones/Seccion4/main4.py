""". Cree un programa que lea un número entre 1 y 15 y muestre si éste es primo o no
Autor: Jesus Aguilar
Fecha: 3 Noviembre 2023"""

# Solicitar al usuario que ingrese un número entre 1 y 15
numero = int(input("Ingrese un número entre 1 y 15: "))

# Verificar si el número es primo o no
if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f"El número {numero} no es primo.")
            break
    else:
        print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
