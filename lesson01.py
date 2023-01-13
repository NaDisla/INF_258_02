# Captura por teclado
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su sueldo: "))

# Impresión por pantalla
print(nombre)

# Concatenación:
print("Su nombre es: "+nombre)

# Otras formas de concatenar (interpolar variables)
print(f"Su nombre es: {nombre}")
print("Su edad es: {edad}".format(edad=edad))
print("Su sueldo es: %s" % sueldo)