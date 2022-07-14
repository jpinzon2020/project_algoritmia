import json


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

        print(f'Calles: \n{json.dumps(self.calles, indent=2)}')

        return None

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

    def agregar_luces_verdes(self, traffic_lights):
        for street in self.calles:
            programmed = False
            for street_programmed in traffic_lights:

                if street[self.indice_nombre_calle] == street_programmed[0]:
                    street.append(street_programmed[1])
                    programmed = True
                    break

            # Si no fue programado, el semaforo nunca esta en verde. Por tanto, su tiempo asignado es cero
            if not programmed:
                street.append(0)

'''
    def calculate_red_lights(self):
        for street in self.streets:
            intersection = street[self.index_to]
            total_time = 0

            for street in
'''


