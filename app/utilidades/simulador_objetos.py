from objetos.calle import Calle
from objetos.interseccion import Interseccion
from objetos.mapa_vial import MapaVial
from objetos.semaforo import Semaforo
from objetos.trayecto import Trayecto


class SimuladorObjetos:

    def __init__(self, puntaje: int, segundos: int, mapa_vial: MapaVial):
        self.puntaje = puntaje
        self.segundos = segundos
        self.mapa_vial = mapa_vial

    def simular(self, intersecciones_programadas: list[Interseccion]) -> int:
        # TO DO
        return 0