from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora

class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        self._idOrden = Orden.aumentarId()
        self._computadoras = list(computadoras)

    @classmethod
    def aumentarId(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    @property
    def idOrden(self):
        return self._idOrden
    
    @property
    def computadoras(self):
        return self._computadoras

    @idOrden.setter
    def idOrden(self, idOrden):
        self._idOrden = idOrden

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = list(computadoras)
    
    def __str__(self):
        computadora_string = ''
        
        for computadora in self._computadoras:
            computadora_string += computadora.__str__()

        return f'''Orden: {self._idOrden}, computadoras:
        {computadora_string}'''


# Para testear
if __name__ == "__main__":
    monitor1 = Monitor("LG", "Chico")
    monitor2 = Monitor("Samsung", "Mediano")
    monitor3 = Monitor("Sony", "Grande")
    raton1 = Raton('USB', 'Razer')
    raton2 = Raton('PS2', 'Genius')
    raton3 = Raton('X', 'Sarasa')
    teclado1 = Teclado('UCV', 'X Factor')
    teclado2 = Teclado('UCW', 'Y Factore')
    teclado3 = Teclado('QCW', 'Z Factori')

    computadora1 = Computadora('HP', monitor3, teclado1, raton1)
    computadora2 = Computadora('Gamer', monitor1, teclado3, raton2)
    computadora3 = Computadora('Casual', monitor2, teclado2, raton3)
    computadorasLista = [computadora1, computadora2]
    orden1 = Orden(computadorasLista)
    computadorasLista = [computadora2]
    orden2 = Orden(computadorasLista)
    orden2.agregarComputadora(computadora3)
    print(orden1)
    print(orden2)