# Excepciones
try: # Este bloque contiene lo que queremos ejecutar.
    result = 20 / 0
    print(result)
except ZeroDivisionError: # Colocamos el tipo de error que estamos manejando.
    print("No se puede dividir por 0")
finally: # Este bloque se ejecutará siempre. Sin importar si la excepción ocurre o no.
    print("Caso por defecto.")

try:
    result = 20 / 0
    print(result)
except ZeroDivisionError:
    raise Exception("Alguna otra excepción que queramos lanzar.")
finally:
    print("Caso por defecto.")