# BUCLE WHILE
n = 1
suma = 0
while n <= 10:
    x = int(input("Digite el %d número:"%n))
    suma = suma + x # ACUMULADOR
    n = n + 1 # CONTADOR
print("Suma: %d" % suma)

# USO DE BREAK Y CONTINUE
s = 0
while True:
    v = int(input("Digite un número a sumar o 0 para salir:"))
    if v == 0:
        break
    elif v == 3:
        continue
    s = s + v
print(s)

# OPERADOR % PARA DETERMINAR EL RESTO
n = 5
if(n%2 == 0):
    print("Es par")
else:
    print("Es impar")