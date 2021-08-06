from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        self._idRaton = Raton.aumentarId()
    
    @classmethod
    def aumentarId(cls):
        cls.contadorRatones += 1
        return cls.contadorRatones

    def __str__(self):
        return f'Ratón: Id: {self._idRaton}, {super().__str__()}'


# Para testear
if __name__ == '__main__':
    raton1 = Raton('USB', 'Razer')
    raton2 = Raton('PS2', 'Genius')
    raton3 = Raton('Bluetooth', 'Sarasa')

    print(raton1)
    print(raton2)
    print(raton3)