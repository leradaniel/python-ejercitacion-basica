from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        self._idTeclado = Teclado.aumentarId()

    @classmethod
    def aumentarId(cls):
        cls.contadorTeclados += 1
        return cls.contadorTeclados

    def __str__(self):
        return f'Teclado: Id: {self._idTeclado}, {super().__str__()}'


# Para testear
if __name__ == '__main__':
    teclado1 = Teclado('USB', 'Generica')
    teclado2 = Teclado('Bluetooth', 'Sarasa')
    teclado3 = Teclado('PS2', 'Pirulo')

    print(teclado1)
    print(teclado2)
    print(teclado3)