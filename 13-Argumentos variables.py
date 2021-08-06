# 13) Función con argumentos variables para multiplicar los valores
# Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos
# variables *args como parámetro de la función y regresar como resultado la multiplicación de todos
# los valores pasados como argumentos.

def multiplicar_valores(*args):
    resultado = 1
    for arg in args:
        resultado *= arg
    return resultado

print(multiplicar_valores(2,5,9,10))