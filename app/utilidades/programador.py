from objetos.calle import Calle
from objetos.interseccion import Interseccion
from objetos.mapa_vial import MapaVial
from objetos.semaforo import Semaforo
from objetos.vehiculo import Vehiculo


class Programador:

    def __init__(self):
        self.numero_intersecciones = 0
        self.numero_calles = 0
        self.numero_vehiculos = 0

    def programar_semaforos_por_tiempo_inicial(self, mapa_vial: MapaVial) -> list[Interseccion]:
        print('Programando semaforos por tiempo inicial')
        self.numero_calles = mapa_vial.cantidad_calles
        self.numero_intersecciones = mapa_vial.cantidad_intersecciones
        self.numero_vehiculos = mapa_vial.cantidad_vehiculos
        calles = mapa_vial.calles
        intersecciones = mapa_vial.intersecciones
        vehiculos = mapa_vial.vehiculos
        intersecciones_programadas = []

        for interseccion in intersecciones:
            calles_entrantes = interseccion.calles_entrantes

            # Contamos cuantos vehiculos inician en cada calle que llega a una interseccion
            for calle in calles_entrantes:
                vehiculos_que_inician_en_calle = 0

                for vehiculo in vehiculos:
                    if vehiculo.trayecto[0] == calle:
                        vehiculos_que_inician_en_calle = vehiculos_que_inician_en_calle + 1

                # Creamos un semaforo para cada calle entrante a esa interseccion, iniciando con un tiempo en verde segun
                # la cantidad de vehiculos que inician su recorrido desde alli.
                semaforo = Semaforo(calle=calle)
                semaforo.duracion_luz_verde = vehiculos_que_inician_en_calle
                interseccion.agregar_semaforo(semaforo)

            # Organizamos los semaforos segun tiempo en verde, para que aquellos que tengan mas vehiculos en espera al
            # momento inicial (es decir, con mas vehiculos que inicien alli) empiecen primero
            interseccion.organizar_semaforos_por_tiempo_descendiente()
            intersecciones_programadas.append(interseccion)

        return intersecciones_programadas
