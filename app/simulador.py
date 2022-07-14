import math


class Simulador:
    indice_desde = 0
    indice_hacia = 1
    indice_nombre_calle = 2
    indice_distancia = 3
    indice_luz_verde = 4
    indice_luz_roja = 5

    def __init__(self, puntaje, segundos, calles, trayectos):
        self.puntaje = puntaje
        self.segundos = segundos
        self.calles = calles
        self.trayectos = trayectos

    def simular(self, traffic_lights):
        self.calcular_distancias()
        self.agregar_luces_verdes(traffic_lights)
        self.calcular_luces_rojas()
        self.imprimir_estado_inicial()

    def agregar_luces_verdes(self, semaforo):
        for calle in self.calles:
            esta_programado = False
            for calle_programada in semaforo:

                if calle[self.indice_nombre_calle] == calle_programada[0]:
                    calle[self.indice_luz_verde] = calle_programada[1]
                    esta_programado = True
                    break

            # Si no fue programado, el semaforo nunca esta en verde y siempre esta en rojo
            if not esta_programado:
                calle[self.indice_luz_verde] = 0
                calle[self.indice_luz_roja] = math.inf

    def calcular_luces_rojas(self):
        i = 0
        while i < len(self.calles):
            j = 0
            aux = self.calles[i]
            interseccion = aux[self.indice_hacia]

            while j < len(self.calles):
                calle = self.calles[j]
                if i != j:
                    if calle[self.indice_hacia] == interseccion:
                        tiempo = aux[self.indice_luz_verde]
                        calle[self.indice_luz_roja] = calle[self.indice_luz_roja] + tiempo

                j = j + 1
            i = i + 1

    def calcular_distancias(self):
        for trayecto in self.trayectos:
            distancia = 0

            i = 1
            while i < len(trayecto):
                for calle in self.calles:
                    if trayecto[i] == calle[self.indice_nombre_calle]:
                        distancia = distancia + calle[self.indice_distancia]

                i = i + 1
            trayecto.insert(0, distancia)

        return self.trayectos

    def imprimir_estado_inicial(self):
        print('\nESTADO INICIAL SEGUN PROGRAMACION\n')
        for calle in self.calles:
            print(f'{calle[self.indice_nombre_calle]} desde {calle[self.indice_desde]} hacia {calle[self.indice_hacia]}\n'
                  f'Distancia: {calle[self.indice_distancia]}, '
                  f'tiempo en verde: {calle[self.indice_luz_verde]}, '
                  f'tiempo en rojo: {calle[self.indice_luz_roja]}\n')
