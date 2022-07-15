import json
from lector import Lector
from escritor import Escritor
from simulador import Simulador
from programacion import Programacion

if __name__ == '__main__':
    _lector = Lector()
    _escritor = Escritor()

    grafo = _lector.leer_como_grafo(r'../data/red.txt')
    # print(f"Grafo {grafo}")

    # Este es el listado de calles. Orden de las posiciones: desde donde sale, para donde va, nombre de la calle, distancia
    calles = _lector.leer_como_lista_de_calles(r'../data/red.txt')
    print(f"Calles {calles}")

    segundos, puntaje = _lector.leer_configuracion(r'../data/simulacion.txt')
    print(f"Segundos {segundos} y puntaje {puntaje}")

    trayectos = _lector.leer_trayectos(r'../data/trayectos.txt')

    _simulador = Simulador(puntaje, segundos, calles, trayectos)
    trayectos = _simulador.calcular_distancias() # Aca se calculan las distancias en cada trayecto, y se ponen en la primera posicion del arreglo

    _programacion = Programacion(trayectos, calles, grafo)
    print(f"Encolamiento de vehiculos {_programacion.cola_vehiculos}")

    print(f"Trayectos {trayectos}")

    programacion = [
        # [nombre_calle, tiempo en verde, posicion en verde]
        # La posicion en verde me dice, si dados 5 semaforos que llegan a una interseccion, en que orden se ponen en verde:
        # de primero, segundo, tercero, cuarto o quinto
        # Evidentemente si solo hay 2 semaforos, si uno empieza en verde, el otro empieza en rojo
        # Se propone
        # [calle1, 10, 2]
        # que indicaria semaforo al final de la calle1, con 10 segundos en verde, y es el segundo en la interseccion en ponerse en verde
        # (o el tercero, si la posicion empieza en 0)
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

    _simulador.simular(programacion)

    # print(f'Archivo guardado en {_writer.crear_reporte(programacion)}')

