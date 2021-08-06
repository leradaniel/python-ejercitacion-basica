# 4) Solicitar al usuario dos valores, y determinar cual número es el mayor
# Solicitar al usuario dos valores:
# numero1 (int)
# numero2 (int)

# Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):

# Proporciona el numero1:
# Proporciona el numero2:
# El numero mayor es:<numeroMayor>

#Cómo lo hice yo:
numero1 = int(input("Proporciona el numero1: "))
numero2 = int(input("Proporciona el numero2: "))
numeroMayor = numero1
if (numero2 > numero1):
    numeroMayor = numero2
print(f"El numero mayor es: {numeroMayor}")