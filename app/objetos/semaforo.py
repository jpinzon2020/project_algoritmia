class Semaforo:

    def __init__(self, calle: str, duracion_luz_verde: int):
        self._calle = calle
        self._duracion_luz_verde = duracion_luz_verde

    @property
    def calle(self):
        return self._calle

    @property
    def duracion_luz_verde(self):
        return self._duracion_luz_verde
