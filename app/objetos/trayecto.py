class Trayecto:

    def __init__(self, cantidad_calles: int):
        self._cantidad_calles = cantidad_calles
        self._calles = []

    def agregar_calle(self, nombre: str):
        self._calles.append(nombre)

    @property
    def cantidad_calles(self):
        return self._cantidad_calles

    @property
    def calles(self):
        if self._calles:
            return self._calles
        return None
