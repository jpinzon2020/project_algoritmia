class Calle:

    def __init__(self, nombre: str, desde: int, hacia: int, distancia: int):
        self._nombre = nombre
        self._desde = desde
        self._hacia = hacia
        self._distancia = distancia

    @property
    def nombre(self):
        return self._nombre

    @property
    def desde(self):
        return self._desde

    @property
    def hacia(self):
        return self._hacia

    @property
    def distancia(self):
        return self._distancia
