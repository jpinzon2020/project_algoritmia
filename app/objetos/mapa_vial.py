from objetos.calle import Calle
from objetos.interseccion import Interseccion
from objetos.trayecto import Trayecto


class MapaVial:

    def __init__(self, cantidad_intersecciones: int, cantidad_calles: int, cantidad_trayectos: int):
        self._cantidad_intersecciones = cantidad_intersecciones
        self._intersecciones = []
        self._cantidad_calles = cantidad_calles
        self._calles = []
        self._cantidad_trayectos = cantidad_trayectos
        self._trayectos = []

    def agregar_calles(self, calles: list[Calle]):
        self._calles = calles

    def agregar_intersecciones(self, intersecciones: list[Interseccion]):
        self._intersecciones = intersecciones

    def agregar_trayectos(self, trayectos: list[Trayecto]):
        self._trayectos = trayectos

    @property
    def cantidad_intersecciones(self):
        return self._cantidad_intersecciones

    @property
    def cantidad_calles(self):
        return self._cantidad_calles

    @property
    def cantidad_trayectos(self):
        return self._cantidad_trayectos

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
    def trayectos(self):
        if self._trayectos:
            return self._trayectos
        return None
