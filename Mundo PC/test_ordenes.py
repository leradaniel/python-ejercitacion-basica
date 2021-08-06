from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

monitor1 = Monitor("LG", "Chico")
monitor2 = Monitor("Samsung", "Mediano")
monitor3 = Monitor("Sony", "Grande")
monitor4 = Monitor("Philips", "Chico")
monitor5 = Monitor("Noblex", "Mediano")

teclado1 = Teclado('USB', 'Corsair')
teclado2 = Teclado('USB', 'Genius')
teclado3 = Teclado('USB', 'Logitech')
teclado4 = Teclado('PS2', 'Noganet')
teclado5 = Teclado('Wireless', 'Dell')

raton1 = Raton('USB', 'Corsair')
raton2 = Raton('PS2', 'Genius')
raton3 = Raton('USB', 'G.Skill')
raton4 = Raton('USB', 'Razer')
raton5 = Raton('Wireless', 'Red Dragon')

computadora1 = Computadora('Gamer', monitor3, teclado1, raton1)
computadora2 = Computadora('Casual', monitor4, teclado4, raton2)
computadora3 = Computadora('Gamer Low-Cost', monitor1, teclado3, raton5)
computadora4 = Computadora('Work', monitor2, teclado5, raton2)
computadora5 = Computadora('Regular', monitor5, teclado4, raton4)

computadoras1 = [computadora3, computadora1, computadora5]
orden1 = Orden(computadoras1)
computadoras2 = [computadora4, computadora2, computadora1]
orden2 = Orden(computadoras2)
orden2.agregarComputadora(computadora3)
print(orden1)
print(orden2)