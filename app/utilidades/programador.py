from objetos.calle import Calle
from objetos.interseccion import Interseccion
from objetos.mapa_vial import MapaVial
from objetos.semaforo import Semaforo
from objetos.trayecto import Trayecto


class Programador:

    def __init__(self):
        self.numero_intersecciones = 0
        self.numero_calles = 0
        self.numero_trayectos = 0

    def programar_semaforos_por_tiempo_inicial(self, mapa_vial: MapaVial) -> list[Interseccion]:
        self.numero_calles = mapa_vial.cantidad_calles
        self.numero_intersecciones = mapa_vial.cantidad_intersecciones
        self.numero_trayectos = mapa_vial.cantidad_trayectos
        calles = mapa_vial.calles
        intersecciones = mapa_vial.intersecciones
        trayectos = mapa_vial.trayectos
        intersecciones_programadas = []

        for interseccion in intersecciones:
            calles_entrantes = interseccion.calles_entrantes

            # Contamos cuantos trayectos inician en cada calle que llega a una interseccion
            for calle in calles_entrantes:
                trayectos_que_inician_en_calle = 0

                for trayecto in trayectos:
                    if trayecto.calles[0] == calle:
                        trayectos_que_inician_en_calle = trayectos_que_inician_en_calle + 1

                # Creamos un semaforo para la calle entrante a esa interseccion, que inicia con un tiempo en verde segun
                # la cantidad de vehiculos que inician su recorrido desde alli. Es decir, segun la cantidad de trayectos
                # que inician en esa calle
                semaforo = Semaforo(calle=calle, duracion_luz_verde=trayectos_que_inician_en_calle)
                interseccion.agregar_semaforo(semaforo)

            # Organizamos los semaforos segun tiempo en verde, para que aquellos que tengan mas vehiculos en espera al
            # momento inicial (es decir, con mas trayectos que inicien alli) empiecen primero
            interseccion.organizar_semaforos_por_tiempo_descendiente()
            intersecciones_programadas.append(interseccion)

        return intersecciones_programadas
