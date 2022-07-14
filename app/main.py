import json
from reader import Reader
from writer import Writer
from simulator import Simulator


if __name__ == '__main__':
    _reader = Reader()
    _writer = Writer()

    graph = _reader.read_as_graph(r'../data/red.txt')
    print(f"Grafo {graph}")

    streets = _reader.read_as_street_list(r'../data/red.txt')
    print(f"Calles {streets}")

    seconds, score = _reader.read_simulation_config(r'../data/simulacion.txt')
    print(f"Segundos {seconds} y score {score}")

    journeys = _reader.read_journeys(r'../data/trayectos.txt')

    _simulator = Simulator(score, seconds, streets, journeys)
    journeys = _simulator.calculate_distances() # Aca se calculan las distancias en cada trayecto, y se ponen en la ultima posicion del arreglo

    print(f"Trayectos {journeys}")

    programacion = [
        ['calle3', 10],
        ['calle5', 8],
        ['calle1', 12],
        ['calle9', 4],
        ['calle10', 7],
        ['calle4', 12],
        ['calle6', 15],
        ['calle2', 20],
        ['calle7', 1]
    ]
    '''
    programacion = [
        [['calle3', 10], ['calle5', 8]],
        [['calle1', 12], ['calle9', 4]],
        [['calle10', 7], ['calle4', 12]],
        [['calle6', 15], ['calle2', 20]],
        [['calle7', 1]]
    ]
    '''

    print(f'Programacion {programacion}')

    _simulator.simulate(programacion)

    # print(f'Archivo guardado en {_writer.create_program_report(programacion)}')

