# 7) Sistema de Calificaciones
# Crear un sistema de calificaciones según se solicita.
# El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

# El usuario proporcionará un valor entre 0 y 10.
# Si está entre 9 y 10: imprimir una A
# Si está entre 8 y menor a 9: imprimir una B
# Si está entre 7 y menor a 8: imprimir una C
# Si está entre 6 y menor a 7: imprimir una D
# Si está entre 0 y menor a 6: imprimir una F
# cualquier otro valor debe imprimir: Valor desconocido

# Por ejemplo:
# Proporciona un valor entre 0 y 10:
# A
nota_numerica = float(input("Ingrese su calificación (0-10): "))
calificacion = None
if 9 <= nota_numerica <= 10:
    calificacion = "A"
elif 8 <= nota_numerica < 9:
    calificacion = "B"
elif 7 <= nota_numerica < 8:
    calificacion = "C"
elif 6 <= nota_numerica < 7:
    calificacion = "D"
elif 0 <= nota_numerica < 6:
    calificacion = "F"

print(f"Nota numérica: {nota_numerica}. Calificación: {calificacion}") if calificacion != None else print("ERROR")