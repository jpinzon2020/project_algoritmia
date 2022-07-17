import math

from objetos.semaforo import Semaforo


class Interseccion:

    def __init__(self, interseccion: int):
        self._interseccion = interseccion
        self._calles_entrantes = []
        self._semaforos = []

        # Los ciclos de cambio indican cuantos segundos transcurren luego de que un semaforo se ponga en rojo
        # para que se vuelva a poner en verde. Si una interseccion no ha sido programada, nunca cambiara a verde,
        # y por tanto, su ciclo es infinito
        self._ciclo_de_cambio = 0

    def agregar_semaforo(self, semaforo: Semaforo):
        self._semaforos.append(semaforo)

    def agregar_calle_entrante(self, calle: str):
        self._calles_entrantes.append(calle)

    def organizar_semaforos_por_tiempo(self):
        self.organizar_por_tiempo(self._semaforos)

    def organizar_semaforos_por_tiempo_descendiente(self):
        self.organizar_por_tiempo(self._semaforos)
        self._semaforos.reverse()

    # Implementacion del algoritmo Merge Sort para organizar los semaforos por su tiempo en verde
    def organizar_por_tiempo(self, semaforos):
        if len(semaforos) > 1:
            mitad = len(semaforos) // 2
            mitad_derecha = semaforos[mitad:]
            mitad_izquierda = semaforos[:mitad]
            self.organizar_por_tiempo(mitad_derecha)
            self.organizar_por_tiempo(mitad_izquierda)

            i = j = k = 0
            while i < len(mitad_izquierda) and j < len(mitad_derecha):
                if mitad_izquierda[i].duracion_luz_verde < mitad_derecha[j].duracion_luz_verde:
                    semaforos[k] = mitad_izquierda[i]
                    i += 1
                else:
                    semaforos[k] = mitad_derecha[j]
                    j += 1
                k += 1

            while i < len(mitad_izquierda):
                semaforos[k] = mitad_izquierda[i]
                i += 1
                k += 1

            while j < len(mitad_derecha):
                semaforos[k] = mitad_derecha[j]
                j += 1
                k += 1

            return semaforos

    @property
    def interseccion(self) -> int:
        return self._interseccion

    @property
    def calles_entrantes(self) -> list:
        return self._calles_entrantes

    @property
    def semaforos(self) -> list[Semaforo]:
        return self._semaforos

    @property
    def ciclo_de_cambio(self) -> int:
        return self._ciclo_de_cambio

    @ciclo_de_cambio.setter
    def ciclo_de_cambio(self, ciclo: int):
        self._ciclo_de_cambio = ciclo
