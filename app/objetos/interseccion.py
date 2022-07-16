from objetos.semaforo import Semaforo


class Interseccion:

    def __init__(self, interseccion: int):
        self._interseccion = interseccion
        self._calles_entrantes = []
        self._semaforos = []

    def agregar_semaforo(self, semaforo: Semaforo):
        self._semaforos.append(semaforo)

    def agregar_calle_entrante(self, calle: str):
        self._calles_entrantes.append(calle)

    @property
    def interseccion(self) -> int:
        return self._interseccion

    @property
    def calles_entrantes(self) -> list:
        return self._calles_entrantes

    @property
    def semaforos(self) -> list[Semaforo]:
        return self._semaforos
