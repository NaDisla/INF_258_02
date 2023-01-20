# Listas
datos = ['Nombre', 'Edad', 'Es_Estudiante'] # Creación de una lista
infos = ['Juan De Los Palotes', 20, False,] # Creación de una lista
print(infos[2]) # Imprimir posición específica

# Crear lista dinámica
cantidad_infos = int(input("Introduzca la cantidad de elementos de la lista: "))
infos_02 = []

# Recorrer lista (bucle for)
for cantidad in range(cantidad_infos):
    info = input("Ingrese la información: ")
    infos_02.append(info) # Agregar items a la lista
print(infos_02) # Imprimir lista comleta

# For anidados
for dato in datos:
    print(dato)
    print("*"*20,"Fin datos")
    for info in infos:
        print(info)
    print("*"*20,"Fin info")

# For básico
for n in range(5):
    print(n)

# Librerías (intro)
import math
raiz = math.sqrt(81)
print(int(raiz))

# Número aleatorio
import random
for dato in range(6):
    codigo_empleado = random.randint(1001,9999)
    print(codigo_empleado)

# Caracteres especiales en strings
print("Imprimimos algo\n")
print("Imprimimosdfshfsjdhdjdsjfshfkfkdfksfk\t\t\t\talgo\t\t039034823")


# Imprimir tabla (ejemplo de librería)
from tabulate import tabulate
table = [["Producto", "Precio", "Cantidad", "Importe"], ["Leche", 45.00, 2, 90.00]]
print(tabulate(table))