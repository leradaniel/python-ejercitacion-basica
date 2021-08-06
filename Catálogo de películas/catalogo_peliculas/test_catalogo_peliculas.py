from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

class Catalogo:
    salir = False
    while (not salir):
        print(f'''1. Agregar película
2. Listar películas
3. Eliminar catálogo de películas
4. Salir''')
        seleccion = input('Escribe tu opción (1-4): ')
        if seleccion == '1':
            nombre_pelicula = input('Proporciona la película: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
            print(f'La película {nombre_pelicula} fue agregada.')
        elif seleccion == '2':
            CatalogoPeliculas.listar_peliculas()
        elif seleccion == '3':
            CatalogoPeliculas.eliminar()
        elif seleccion == '4':
            salir = True
        else:
            print('Opción inválida.')
    else:
        print('Programa finalizado'.center(50,"-"))