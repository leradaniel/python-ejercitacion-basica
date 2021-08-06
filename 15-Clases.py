# 15) Calcular el área de un rectángulo con las medidas ingresadas por el usuario.
# Debe tener una clase Rectángulo, los atributos Altura / Base y un método CalcularArea
# La fórmula para calcular el área es A = b x h
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area
        # Se puede resumir en una linea:
        # return self.base * self.altura

base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura: "))
rectangulo_creado = Rectangulo(base,altura)
print(f'El área del rectángulo es de {rectangulo_creado.calcular_area()}')