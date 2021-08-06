# Clase de servicio
import os

class CatalogoPeliculas:
    ruta_archivo = 'Catálogo de películas\\catalogo_peliculas\\peliculas.txt'

    @staticmethod
    def agregar_pelicula(pelicula):
        with open(CatalogoPeliculas.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(pelicula.nombre + '\n')

    @staticmethod
    def listar_peliculas():
        with open(CatalogoPeliculas.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catálogo de películas'.center(50, "-"))
            print(archivo.read())

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print(f'Archivo eliminado: {CatalogoPeliculas.ruta_archivo}')
        except Exception as e:
            print(f'Ocurrió un error: {e}, {type(e)}')