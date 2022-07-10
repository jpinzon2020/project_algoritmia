from pathlib import Path


class Reader:
    directory = Path(__file__).parent

    def read_journeys(self, file):
        i = 0
        filepath = (self.directory / file).resolve()
        with open(f'{filepath}', 'r') as f:
            for line in f:
                values = line.split()

                if i == 0:
                    journeys = [None] * int(values[0])
                else:
                    journeys[i - 1] = values

                i = i + 1

        return journeys

    def read_graph(self, file):
        i = 0
        vertices = []

        filepath = (self.directory / file).resolve()
        with open(f'{filepath}', 'r') as f:
            for line in f:
                values = line.split()

                if i == 0:
                    vertices_number = int(values[0])

                    for j in range(vertices_number):
                        vertices.append([])
                else:
                    from_vertice = int(values[0])
                    to_vertice = int(values[1])
                    street_name = values[2]
                    time_to_walk_it = int(values[3])

                    adjacency = [to_vertice, street_name, time_to_walk_it]

                    adjacencies = vertices[from_vertice]
                    adjacencies.append(adjacency)
                    vertices[from_vertice] = adjacencies

                i = i + 1

        return vertices

