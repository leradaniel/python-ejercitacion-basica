class Monitor():
    contadorMonitores = 0

    def __init__(self, marca, tamaño):
        self._marca = marca
        self._tamaño = tamaño
        self._idMonitor = Monitor.aumentarId()

    @classmethod
    def aumentarId(cls):
        cls.contadorMonitores +=1
        return cls.contadorMonitores

    @property
    def marca(self):
        return self._marca

    @property
    def tamaño(self):
        return self._tamaño

    @property
    def idMonitor(self):
        return self._idMonitor

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    @idMonitor.setter
    def idMonitor(self, idMonitor):
        self._idMonitor = idMonitor

    def __str__(self):
        return f'Monitor: Id: {self._idMonitor}, marca: {self._marca}, tamaño: {self._tamaño}'


# Para testear
if __name__ == "__main__":
    monitor1 = Monitor("LG", "Chico")
    monitor2 = Monitor("Samsung", "Mediano")
    monitor3 = Monitor("Sony", "Grande")

    print(monitor1)
    print(monitor2)
    print(monitor3)

    monitor1.tamaño = "Descomunal"
    print(monitor1.tamaño)
    monitor2.marca = "Sorny"
    print(monitor2.marca)
    monitor3.idMonitor = 8
    print(monitor3.idMonitor)