"""Cree un programa que pregunte al usuario si desea salir, si o no “S/N”, si el usuario teclea la letra S el
programa se detendrá, de lo contrario continuará ejecutándose.

Autor: Jesus Aguilar"""

# Pregunta al usuario si desea salir

seguir = True
while seguir:
    respuesta = input("¿Desea salir? (S/N): ").upper()
    if respuesta == "S":
        seguir = False
    else:
        print("Continuando...")
