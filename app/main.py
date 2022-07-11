from reader import Reader
from writer import Writer

_reader = Reader()
_writer = Writer()


if __name__ == '__main__':
    print(f"Grafo {_reader.read_graph(r'../data/red.txt')}")

    print(f"Trayectos {_reader.read_journeys(r'../data/trayectos.txt')}")

    seconds, score = _reader.read_simulation_config(r'../data/simulacion.txt')
    print(f"Segundos {seconds} y score {score}")

    programacion = [
        [['calle3', 10], ['calle5', 8]],
        [['calle1', 12], ['calle9', 4]],
        [['calle10', 7], ['calle4', 12]],
        [['calle6', 15], ['calle2', 20]],
        [['calle7', 1]]
    ]
    print(f'Archivo guardado en {_writer.create_program_report(programacion)}')

