import math


class Semaforo:

    def __init__(self, calle: str):
        self._calle = calle
        self._duracion_luz_verde = 0

        # Todos los semaforos tardan un tiempo en ponerse en verde por primera vez. Ello depende de la progamacion,
        # y la posicion en que se cambien
        self._primer_segundo_en_verde = math.inf

    @property
    def calle(self):
        return self._calle

    @property
    def duracion_luz_verde(self) -> int:
        return self._duracion_luz_verde

    @property
    def primer_segundo_en_verde(self) -> int:
        return self._primer_segundo_en_verde

    @duracion_luz_verde.setter
    def duracion_luz_verde(self, duracion_luz_verde: int):
        self._duracion_luz_verde = duracion_luz_verde

    @primer_segundo_en_verde.setter
    def primer_segundo_en_verde(self, primer_segundo_en_verde: int):
        self._primer_segundo_en_verde = primer_segundo_en_verde
