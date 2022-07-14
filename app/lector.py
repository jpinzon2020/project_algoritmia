from pathlib import Path


class Lector:
    directorio = Path(__file__).parent

    def leer_como_grafo(self, archivo):
        i = 0
        graph = []

        filepath = (self.directorio / archivo).resolve()
        with open(f'{filepath}', 'r') as f:
            for line in f:
                values = line.split()

                # Inicializamos el grafo segun la cantidad de vertices (intersecciones) que se encuentren
                if i == 0:
                    intersection_count = int(values[0])

                    for j in range(intersection_count):
                        graph.append([])
                else:
                    # Agregamos una calle que va desde una interseccion hacia otra interseccion, que tiene un nombre
                    # y un tiempo para recorrerla
                    from_vertice = int(values[0])
                    to_vertice = int(values[1])
                    street_name = values[2]
                    time_to_walk_it = int(values[3])

                    adjacency = [to_vertice, time_to_walk_it, street_name]

                    adjacencies = graph[from_vertice]
                    adjacencies.append(adjacency)
                    graph[from_vertice] = adjacencies

                i = i + 1

        f.close()

        return graph

    def leer_como_lista_de_calles(self, file):
        i = 0
        streets = []

        filepath = (self.directorio / file).resolve()
        with open(f'{filepath}', 'r') as f:
            for line in f:
                values = line.split()

                if i == 0:
                    streets = [None] * int(values[1])
                else:
                    # Agregamos una calle que va desde una interseccion hacia otra, que tiene un nombre
                    # y un tiempo para recorrerla
                    from_intersection = int(values[0])
                    to_intersection = int(values[1])
                    street_name = values[2]
                    time_to_walk_it = int(values[3])

                    street = [from_intersection, to_intersection, street_name, time_to_walk_it]

                    streets[i - 1] = street

                i = i + 1

        f.close()

        return streets

    def read_journeys(self, file):
        i = 0
        filepath = (self.directorio / file).resolve()
        with open(f'{filepath}', 'r') as f:
            for line in f:
                values = line.split()

                if i == 0:
                    # Inicializamos la cantidad de trayectos segun la cantidad dada en la primera posicion
                    journeys = [None] * int(values[0])
                else:
                    journeys[i - 1] = values

                i = i + 1
        f.close()

        return journeys

    def leer_configuracion(self, file):
        filepath = (self.directorio / file).resolve()

        with open(f'{filepath}', 'r') as f:
            seconds = int(f.readline())
            score = int(f.readline())
            f.close()

        return seconds, score
