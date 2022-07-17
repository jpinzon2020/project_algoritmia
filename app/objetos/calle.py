class Calle:

    def __init__(self, nombre: str, desde: int, hacia: int, distancia: int):
        self._nombre = nombre
        self._desde = desde
        self._hacia = hacia
        self._distancia = distancia
        self._cola_de_vehiculos = []

    def agregar_vehiculo(self, identificador_vehiculo: int):
        self._cola_de_vehiculos.append(identificador_vehiculo)

    def liberar_vehiculo(self):
        self._cola_de_vehiculos.pop(0)

    def primer_vehiculo(self):
        return self._cola_de_vehiculos[0]

    def remover_vehiculo(self, identificador_vehiculo: int):
        self._cola_de_vehiculos.remove(identificador_vehiculo)

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
