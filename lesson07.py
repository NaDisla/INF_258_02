# DICCIONARIOS:
menu = {
    "avena": 3, 
    "tostada": 6, 
    "zumo": 5, 
    "muffin": 2
}
nuevo_alimento = input("Nuevo alimento: ")
precio = float(input("Precio: "))
menu[nuevo_alimento] = precio
print(menu)
menu["pan"] = 10.0
print(menu["zumo"])
for key, value in menu.items():
    print(key, value)

for k in menu.keys():
    print(k)

for v in menu.values():
    print(v)

# TUPLAS:
lista = ['Daniel', 'Medellin', 'Programmer', 3]
tupla = tuple(lista)
my_info = ('Daniel', 'Medellin', 'Programmer', 3)
for i in my_info:
    print(i)

# SETS:
lista_duplicados = ["pablo", "ana", "andrea", "andrea"]
nuevo_set = set(lista_duplicados)
for i in nuevo_set:
    print(i)