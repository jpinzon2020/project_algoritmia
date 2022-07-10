from app.reader import Reader

_reader = Reader()


if __name__ == '__main__':
    #print(load.load_graph())
    #print(load.load_graph())
    print(_reader.read_journeys(r'../data/trayectos.txt'))

