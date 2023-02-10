"""
Primer caracter que no se repite. Dada una cadena de caracteres (sin espacios), mostrar el primer caracter que no se repite.
Ejemplo:

Ingrese una cadena de caracteres: aaabbbcdxdefefef

El primer caracter que no se repite es: c
"""
cadena = input("Ingrese una cadena de caracteres sin espacios: ")
uniques = []

for c in cadena:
    char_count = cadena.count(c)
    if char_count > 1:
        continue
    else:
        uniques.append(c)

result = uniques[0]
print("El primer caracter que no se repite es %s" % result)

"""
Números FizzBuzz. Dado un número mayor a 10, realizar la suma de sus dígitos. Con el resultado de la suma, realizar lo siguiente:
Generar los números del 1 al s (suma), y a su vez hacer las siguientes condiciones:
Si el número es divisible por 3, mostrar el número y la palabra "Fizz".
Si el número es divisible por 5, mostrar el número y la palabra "Buzz".
Si el número es divisible por 3 y 5 (ambos), mostrar el número y la palabra "FizzBuzz".
Si el número no es divisible por ninguno (3 y 5), únicamente mostrar el número.
"""
number = input("Ingrese un número mayor a 10: ")

if int(number) > 10:
    result = 0
    for n in number:
        result += int(n)
    print("La suma de los dígitos es: %s" % result)
    for i in range(1, result + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("%s FizzBuzz" % i)
        elif i % 3 == 0:
            print("%s Fizz" % i)
        elif i % 5 == 0:
            print("%s Buzz" % i)
        else:
            print("%s" % i)
else:
    print("Debes ingresar un número mayor a 10.")
