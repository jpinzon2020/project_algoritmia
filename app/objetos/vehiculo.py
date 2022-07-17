class Vehiculo:
    _estado_en_transito = 'EN TRANSITO'
    _estado_llegada = 'LLEGADA'

    # Cuando se crea un vehiculo, se crea con un identificador, y la calle por la que viaja, que es la numero 0 de su recorrido.
    # Segun el problema, el vehiculo inicia al final de la calle de la que parte.
    # Por tanto, el tiempo restante en dicha calle es 0, y esta en transito a su destino
    def __init__(self, identificador: int, cantidad_calles: int):
        self._identificador = identificador
        self._cantidad_calles = cantidad_calles
        self._trayecto = []
        self._viaja_por_calle = 0
        self._tiempo_restante = 0
        self._estado = self._estado_en_transito

    '''
    Funcion mediante la que el vehiculo avance. Ese avance puede indicar reducir el tiempo en la calle actual,
    o cruzar una interseccion, por lo cual la calle por la que viaja es diferente
    '''
    def avanzar(self):
        # Un vehiculo solo puede avanzar si se encuentra En Transito
        if self._estado == self._estado_en_transito:

            # Si le queda tiempo por moverse en la calle actual, entonces el vehiculo reduce ese tiempo en 1 segundo
            # cuando avanza
            if self._tiempo_restante > 0:
                self._tiempo_restante -= 1

            # Si no hay tiempo restante, y se encuenta En transito, el vehiculo estaba en espera de cruzar una interseccion
            # de modo que ahora le queda por recorrer la distancia en tiempo de la calle a la que avanza.
            elif self._tiempo_restante == 0:
                self._viaja_por_calle += 1

            self.evaluar_estado()

    def evaluar_estado(self):
        # Si al vehiculo no le queda tiempo por moverse, y se encuentra en la calle final, entonces ha terminado
        # su recorrido
        if self._tiempo_restante == 0 and self._viaja_por_calle == self._cantidad_calles:
            self._estado = self._estado_llegada

    def agregar_calle_a_trayecto(self, nombre: str):
        self._trayecto.append(nombre)

    def sigue_en_transito(self) -> bool:
        if self._estado == self._estado_en_transito:
            return True
        else:
            return False

    @property
    def identificador(self) -> int:
        return self._identificador

    @property
    def calle_actual(self) -> str:
        if self._viaja_por_calle >= self._cantidad_calles:
            # Retornar la ultima calle del trayecto
            return self._trayecto[self._cantidad_calles - 1]

        return self._trayecto[self._viaja_por_calle]

    @property
    def cantidad_calles(self) -> int:
        return self._cantidad_calles

    @property
    def tiempo_restante(self) -> int:
        return self._tiempo_restante

    @property
    def trayecto(self):
        if self._trayecto:
            return self._trayecto
        return None

    @tiempo_restante.setter
    def tiempo_restante(self, tiempo: int):
        self._tiempo_restante = tiempo
