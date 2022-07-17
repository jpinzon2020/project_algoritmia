from objetos.calle import Calle
from objetos.interseccion import Interseccion
from objetos.vehiculo import Vehiculo


class MapaVial:

    def __init__(self, cantidad_intersecciones: int, cantidad_calles: int, cantidad_vehiculos: int):
        self._cantidad_intersecciones = cantidad_intersecciones
        self._intersecciones = []
        self._cantidad_calles = cantidad_calles
        self._calles = []
        self._cantidad_vehiculos = cantidad_vehiculos
        self._vehiculos = []

    def agregar_calles(self, calles: list[Calle]):
        self._calles = calles

    def agregar_intersecciones(self, intersecciones: list[Interseccion]):
        self._intersecciones = intersecciones

    def agregar_vehiculos(self, vehiculos: list[Vehiculo]):
        self._vehiculos = vehiculos

    '''
    Retorna la distancia en tiempo para recorrer una calle
    '''
    @staticmethod
    def distancia_de(self, nombre_calle: str) -> int:
        calle = next(x for x in self._calles if x.nombre == nombre_calle)
        return calle.distancia

    @property
    def cantidad_intersecciones(self):
        return self._cantidad_intersecciones

    @property
    def cantidad_calles(self):
        return self._cantidad_calles

    @property
    def cantidad_vehiculos(self):
        return self._cantidad_vehiculos

    @property
    def intersecciones(self):
        if self._intersecciones:
            return self._intersecciones
        return None

    @property
    def calles(self):
        if self._calles:
            return self._calles
        return None

    @property
    def vehiculos(self):
        if self._vehiculos:
            return self._vehiculos
        return None
