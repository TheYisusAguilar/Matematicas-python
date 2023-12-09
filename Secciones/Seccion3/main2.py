"""En un supermercado se tiene los siguientes productos:lentejas
arroz,crema y vino.Las lentejas y el arroz no pagan IVA, el vino y la crema si
Cree un programa que reciba el nombre de alguno de los productos mencionados y muestre si el producto
paga IVA o no
Autor: Jesus Aguilar
Fecha: 25 Octubre 2023"""

#Definir los productos y su estado si pagan IVA 
productos = {
    "Arroz": False,
    "Lentejas": False,
    "Crema": True,
    "Vino": True
}

#Aqui el usuario selecciona el producto
producto_seleccionado = input("Seleccione un producto (arroz, lentejas, crema, vino): ")

if producto_seleccionado in productos:
    if productos[producto_seleccionado]:
        print("El producto seleccionado paga IVA.")
    else:
        print("El producto seleccionado no paga IVA.")
else:
        print("Producto no encontrado. Por favor, seleccione un producto válido.")