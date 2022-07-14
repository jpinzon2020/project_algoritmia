import json


class Simulador:
    index_from = 0
    index_to = 1
    index_street_name = 2
    index_distance = 3
    index_green_light = 4
    index_red_light = 5

    def __init__(self, score, seconds, streets, journeys):
        self.score = score
        self.seconds = seconds
        self.streets = streets
        self.journeys = journeys

    def simular(self, traffic_lights):
        self.calcular_distancias()
        self.agregar_luces_verdes(traffic_lights)

        print(f'Calles: \n{json.dumps(self.streets, indent=2)}')

        return None

    def calcular_distancias(self):
        for journey in self.journeys:
            distance = 0

            i = 1
            while i < len(journey):
                for street in self.streets:
                    if journey[i] == street[self.index_street_name]:
                        distance = distance + street[self.index_distance]

                i = i + 1
            journey.append(distance)

        return self.journeys

    def agregar_luces_verdes(self, traffic_lights):
        for street in self.streets:
            programmed = False
            for street_programmed in traffic_lights:

                if street[self.index_street_name] == street_programmed[0]:
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


