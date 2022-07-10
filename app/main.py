from reader import Reader

_reader = Reader()


if __name__ == '__main__':
    print(f"Grafo {_reader.read_graph(r'../data/red.txt')}")

    print(f"Trayectos {_reader.read_journeys(r'../data/trayectos.txt')}")

    seconds, score = _reader.read_simulation_config(r'../data/simulacion.txt')
    print(f"Segundos {seconds} y score {score}")

