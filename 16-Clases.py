# 16) Calcular el volumen de un cubo con las medidas ingresadas por el usuario.
# La fórmula para calcular el volumen es v = ancho x alto x profundidad
class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

ancho = int(input('Ingrese el ancho del cubo: '))
alto = int(input('Ingrese el alto del cubo: '))
profundidad = int(input('Ingrese la profundidad del cubo: '))
cubo_creado = Cubo(ancho, alto, profundidad)
print(f'El volúmen del cubo es de {cubo_creado.calcular_volumen()}')