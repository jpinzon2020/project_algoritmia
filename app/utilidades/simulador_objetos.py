from objetos.calle import Calle
from objetos.interseccion import Interseccion
from objetos.mapa_vial import MapaVial
from objetos.semaforo import Semaforo
from objetos.vehiculo import Vehiculo

'''
Simulador de Objetos, usado para calcular la programacion de los semaforos
cuando las calles y los trayectos estan definidos como objetos. Calcula correctamente los puntajes, pero requiere optimizacion
'''


class SimuladorObjetos:
    _intersecciones_programadas = []

    def __init__(self, puntaje: int, segundos: int, mapa_vial: MapaVial, memoria: list[dict]):
        self.puntaje = puntaje
        self.segundos = segundos
        self.mapa_vial = mapa_vial

        # Memoria para optimizar consultas. Se encuentra en version inicial, y consiste en un mapa llave - valor
        # tal que la llave es el nombre de la calle, y los valores son su interseccion inicial y final, la distancia, y
        # una cola de vehiculos que estan en ella
        self.memoria = memoria

    def simular(self, intersecciones_programadas: list[Interseccion]) -> int:
        self._intersecciones_programadas = intersecciones_programadas
        self.inicializar_semaforos()
        self.inicializar_calles()

        print(f'Simulando programacion con {len(intersecciones_programadas)} intersecciones programadas')

        vehiculos = self.mapa_vial.vehiculos
        self.puntaje = self.segundos * len(vehiculos)
        print(f'Puntaje inicial: {self.puntaje}')

        # Hacemos la simulacion con cada segundo que transcurre
        segundo_actual = 0
        while segundo_actual <= self.segundos:
            print(f'Segundo : {segundo_actual}')

            for vehiculo in vehiculos:
                if vehiculo.sigue_en_transito():
                    if vehiculo.tiempo_restante == 0:
                        self.evaluar_si_cruza_interseccion(vehiculo, segundo_actual)
                    else:
                        vehiculo.avanzar()
                        self.evaluar_si_termina_recorrido(vehiculo, segundo_actual)

            segundo_actual += 1

        return self.puntaje


    def inicializar_semaforos(self):
        print('Inicializando semaforos')
        for interseccion in self._intersecciones_programadas:
            ciclo = 0
            tiempo_para_iniciar_en_verde = 0

            # Todos los semaforos tardan un tiempo para ponerse en verde por primera vez. Ese tiempo depende del orden
            # en que se ponen en verde, dada su posicion, y del tiempo que ha transcurrido
            posicion = 0
            semaforos = interseccion.semaforos
            while posicion < len(semaforos):
                semaforo = semaforos[posicion]

                tiempo_luz_verde = semaforo.duracion_luz_verde
                ciclo = ciclo + tiempo_luz_verde
                semaforo.primer_segundo_en_verde = tiempo_para_iniciar_en_verde

                tiempo_para_iniciar_en_verde = tiempo_para_iniciar_en_verde + semaforo.duracion_luz_verde
                posicion += 1

            if ciclo != 0:
                interseccion.ciclo_de_cambio = ciclo

    def inicializar_calles(self):
        print('Inicializando calles')
        for vehiculo in self.mapa_vial.vehiculos:
            primera_calle = vehiculo.calle_actual
            self.enfilar_vehiculo(nombre_calle=primera_calle, identificador_vehiculo=vehiculo.identificador)

    def enfilar_vehiculo(self, nombre_calle: str, identificador_vehiculo: int):
        calle = self.memoria.get(nombre_calle)
        calle['cola_de_vehiculos'].append(identificador_vehiculo)

    def remover_primer_vehiculo(self, nombre_calle: str):
        calle = self.memoria.get(nombre_calle)
        calle['cola_de_vehiculos'].pop(0)

    def remover_vehiculo(self, nombre_calle: str, identificador_vehiculo: int):
        calle = self.memoria.get(nombre_calle)
        try:
            # Si el vehiculo existe en la calle, lo remueve
            # Existen casos, para los que un vehiculo solamente cruza una interseccion y termina el recorrido
            # (casos en que el trayecto especificado es de una sola calle), y en tal caso, el vehiculo no existe en la
            # calle en que inicia
            calle['cola_de_vehiculos'].remove(identificador_vehiculo)
        except ValueError as e:
            pass

    def evaluar_si_cruza_interseccion(self, vehiculo: Vehiculo, segundo_actual: int):
        nombre_calle_actual = vehiculo.calle_actual
        calle = self.memoria.get(nombre_calle_actual)

        # Evaluar si no existen otros vehiculos en la calle antes que el actual
        if calle['cola_de_vehiculos'][0] == vehiculo.identificador:
            interseccion = calle['hacia']
            interseccion_programada = next(i for i in self._intersecciones_programadas if interseccion == i.interseccion)

            if interseccion_programada:
                ciclo = interseccion_programada.ciclo_de_cambio

                semaforo = next(s for s in interseccion_programada.semaforos if s.calle == nombre_calle_actual)
                tiempo_en_verde = semaforo.duracion_luz_verde
                primer_segundo_verde_del_semaforo = semaforo.primer_segundo_en_verde

                # Cada semaforo inicia en verde segun haya transcurrido X segundos en verde de los demas semaforos en la misma
                # interseccion. Asi por ejemplo, un semaforo que esta en la segunda posicion se pone en verde luego de que
                # finalice el tiempo en verde del primer semaforo.
                # Luego, para volver a ponerse en verde, debe transcurrir un ciclo completo de cambios en la interseccion.

                # Por ejemplo, para una interseccion en que haya 3 semaforos A, B y C con tiempos en verde de 2, 4 y 5 segundos
                # respectivamente, el semaforo B se pondra en verde por primera vez en el segundo numero 2 (cuando ha finalizado
                # el primer semaforo A). B se pondra rojo en segundo numero 6 (cuando han pasado sus 4 segundos asignados),
                # y volvera a estar en verde nuevamente cuando los semaforos C y A han cumplido sus tiempos, es decir, tras
                # 7 segundos.
                # El semaforo B estara activo en el segundo 13 (7 segundos, mas los 6 que habian transcurrido la primera vez).

                # Deducimos que cada semaforo se pone en verde en el segundo s con la formula F1:
                # s = sp + (c * n)
                # sp: segundo en que se pone en verde por primera vez
                # c: ciclo de la interseccion
                # n: iteracion en que el ciclo se realiza

                # Para el ejemplo anterior, el semaforo B se pondria en verde en los segundos:
                # 2 + (11 * 0) = 2
                # 2 + (11 * 1) = 13
                # 2 + (11 * 2) = 24
                # 2 + (11 * 3) = 35 y asi, sucesivamente

                # Por tanto, si quiero saber si un vehiculo tiene el semaforo en verde en un instante de tiempo T,
                # se puede deducir si T esta en un rango valido de tiempo, tal que
                # T / c = n
                # En donde la iteracion se obtiene al dividir el segundo actual entre el ciclo de la interseccion.

                # Si, al evaluar en la formula F1 obtenemos que el segundo actual esta en el rango [si - sj],
                # donde sj = si + v, con v tiempo en verde, podemos afirmar que el vehiculo tiene en verde dicho semaforo
                # en el segundo T.
                iteracion = segundo_actual // ciclo

                tiempo_iteracion = primer_segundo_verde_del_semaforo + (ciclo * iteracion)
                tiempo_maximo_iteracion = tiempo_iteracion + tiempo_en_verde

                # El segundo actual debe estar en el rango de la iteracion, y por tanto el vehiculo puede avanzar
                if tiempo_iteracion <= segundo_actual < tiempo_maximo_iteracion:
                    self.remover_primer_vehiculo(vehiculo.calle_actual)
                    vehiculo.avanzar()
                    if not self.evaluar_si_termina_recorrido(vehiculo, segundo_actual):
                        vehiculo.tiempo_restante = calle['distancia']
                        self.enfilar_vehiculo(nombre_calle=vehiculo.calle_actual, identificador_vehiculo=vehiculo.identificador)

    '''
    Evalua si el vehiculo termina el recorrido en el segundo actual, y agrega el puntaje correspondiente
    '''
    def evaluar_si_termina_recorrido(self, vehiculo: Vehiculo, segundo_actual: int):
        # Si el vehiculo no sigue en transito, ha terminado su recorrido. Por tanto, se elimina de la calle en que se
        # encuentra y se puede agregar el puntaje
        if not vehiculo.sigue_en_transito():
            self.remover_vehiculo(nombre_calle=vehiculo.calle_actual, identificador_vehiculo=vehiculo.identificador)
            self.puntaje = self.puntaje + (self.segundos - segundo_actual)
            print(f'Vehiculo {vehiculo.identificador} termina trayecto. Puntaje acumulado: {self.puntaje}')
            return True
        return False
