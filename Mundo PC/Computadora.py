from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor

class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        self._idComputadora = Computadora.aumentarId()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @classmethod
    def aumentarId(cls):
        cls.contadorComputadoras += 1
        return cls.contadorComputadoras

    @property
    def idComputadora(self):
        return self._idComputadora
    
    @idComputadora.setter
    def idComputadora(self, idComputadora):
        self._idComputadora = idComputadora

    @property
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
        return self._raton

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''{self._nombre}: {self._idComputadora}
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''


# Para testear
if __name__ == "__main__":
    monitor1 = Monitor("LG", "Chico")
    monitor2 = Monitor("Samsung", "Mediano")
    monitor3 = Monitor("Sony", "Grande")
    raton1 = Raton('USB', 'Razer')
    teclado1 = Teclado('Wireless', 'X Factor')

    computadora1 = Computadora('HP', monitor3, teclado1, raton1)
    print(computadora1)