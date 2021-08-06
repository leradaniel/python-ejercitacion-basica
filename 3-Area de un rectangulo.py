# 3) En el siguiente ejercicio se solicita calcular el área y perímetro de un Rectángulo
# Para ello deberemos crear las siguientes variables:
# alto (int)
# ancho (int)

# El usuario debe proporcionar los valores de largo y ancho, y después se debe imprimir el resultado en el siguiente formato(no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

# Proporciona el alto:
# Proporciona el ancho:
# Area: <area>
# Perímetro: <perimetro>
# Las fórmulas para calcular el área y el perímetro de un Rectángulo son:

# Área: alto * ancho

# Perímetro: (alto + ancho) * 2

alto = int(input("Proporciona el alto (número entero): "))
ancho = int(input("Proporciona el ancho (número entero): "))
area = alto * ancho
print(f"Area: {area}")
perimetro = (alto + ancho) * 2
print(f"Perimetro: {perimetro}")