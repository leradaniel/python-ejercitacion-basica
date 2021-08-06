# 18) Crear varios objetos del tipo Cuadrado y Rectángulo, definiendo las siguientes clases:

# FiguraGeometrica (Clase Padre encapsulada):
# -Atributos encapsulados (alto, ancho)
# -Métodos ( __init__(), __str__, get_alto(), set_alto(alto), get_ancho, set_ancho(ancho) )

# Color (Clase Padre encapsulada):
# -Atributos encapsulados ( color )
# -Métodos ( get_color(), set_color(color) )

# Cuadrado (Clase Hija de FiguraGeometrica y Color)
# -Métodos ( __init__(), __str__(), area() )    El área de un cuadrado es lado * lado

# Rectangulo  (Clase Hija de FiguraGeometrica y Color)
# -Métodos ( __init__(), __str__(), area() )    El área de un rectángulo es base * altura
class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho
    
    def __str__(self):
        return f'Alto: {self._alto}. Ancho: {self._ancho}.'

    @property
    def alto(self):
        return self._alto

    @property
    def ancho(self):
        return self._ancho

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color: {self._color}.'

#from Color import Color
#from FiguraGeometrica import FiguraGeometrica
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return (self._alto * self._ancho)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

#from Color import Color
#from FiguraGeometrica import FiguraGeometrica
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, base, altura, color):
        FiguraGeometrica.__init__(self, altura, base)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return (self._alto * self._ancho)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

cuadrado1 = Cuadrado(5, 'Verde')
print('Creación de un cuadrado'.center(50, '-'))
print(cuadrado1)
print(f'Area cuadrado: {cuadrado1.calcular_area()}')

print('Creación de un cuadrado'.center(50, '-'))
cuadrado2 = Cuadrado(25, 'Rojo')
print(cuadrado2)
print(f'Area cuadrado: {cuadrado2.calcular_area()}')

print('Creación de un rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(25, 5, "Azul")
print(rectangulo1)
print(f'Area rectángulo: {rectangulo1.calcular_area()}')

print('Creación de un rectángulo'.center(50, '-'))
rectangulo2 = Rectangulo(101, 8, "Blanco")
print(rectangulo2)
print(f'Area rectángulo: {rectangulo2.calcular_area()}')