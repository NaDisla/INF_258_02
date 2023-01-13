# ===================== CONDICIONALES =====================
num01 = int(input("Ingrese el primer número: "))
num02 = int(input("Ingrese el segundo número: "))
num03 = int(input("Ingrese el tercer número: "))

if(num01 > num02 and num01 > num03):
    print("El primer número es el mayor de todos.")
elif(num02 > num01 and num02 > num03):
    print("El segundo número es el mayor de todos.")
else:
    print("El tercer número es el mayor de todos.")
print("Se acabó el programa")

nombre = input("Ingrese su nombre: ")
if(not nombre.endswith("a")):
    print("El nombre no termina con a")
else:
    print("El nombre termina con a")

# ===================== Formato de decimales para 2 posiciones =====================

nota = 2 / 3
print(f"{round(nota,2)}")