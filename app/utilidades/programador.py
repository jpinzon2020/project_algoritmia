from objetos.calle import Calle
from objetos.interseccion import Interseccion
from objetos.mapa_vial import MapaVial
from objetos.semaforo import Semaforo
from objetos.trayecto import Trayecto


class Programador:

    def __init__(self, puntaje: int, segundos: int):
        self.puntaje = puntaje
        self.segundos = segundos
        self.intersecciones = []
        self.numero_intersecciones = 0
        self.numero_calles = 0
        self.numero_trayectos = 0

    def simular(self, mapa_vial: MapaVial):
        self.numero_calles = mapa_vial.cantidad_calles
        self.numero_intersecciones = mapa_vial.cantidad_intersecciones
        self.numero_trayectos = mapa_vial.cantidad_trayectos
        calles = mapa_vial.calles
        trayectos = mapa_vial.trayectos

        intersecciones = []
        for calle in calles:
            if calle.hacia not in intersecciones:
                intersecciones.append(calle.hacia)


        print(f'TENEMOS intersec {intersecciones}')

        print(f'TENEMOS calles {self.numero_calles} y trayectos {self.numero_trayectos}')

        # TO DO
        return None