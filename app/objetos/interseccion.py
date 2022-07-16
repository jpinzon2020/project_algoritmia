from objetos.semaforo import Semaforo


class Interseccion:

    def __init__(self, interseccion: int, calles_entrantes: int, semaforos: list[Semaforo]):
        self._interseccion = interseccion
        self._calles_entrantes = calles_entrantes
        self._semaforos = []

    def agregar_semaforo(self, semaforo: Semaforo):
        self._semaforos.append(semaforo)

    @property
    def interseccion(self):
        return self._interseccion

    @property
    def calles_entrantes(self):
        return self._calles_entrantes

    @property
    def semaforos(self):
        return self._semaforos
