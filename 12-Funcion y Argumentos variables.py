# 12) Tarea: Función con argumentos variables para sumar todos los valores recibidos
# Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos
# variables *args como parámetro de la función y regresar como resultado la suma de todos
# los valores pasados como argumentos.
def sumar(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma

print(sumar(1,3,5,2,10))