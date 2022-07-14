import json
from lector import Lector
from escritor import Escritor
from simulador import Simulador
from programacion import Programacion

if __name__ == '__main__':
    _lector = Lector()
    _escritor = Escritor()

    grafo = _lector.leer_como_grafo(r'../data/red.txt')
    print(f"Grafo {grafo}")

    # Este es el listado de calles. Orden de las posiciones: desde donde sale, para donde va, nombre de la calle, distancia
    calles = _lector.leer_como_lista_de_calles(r'../data/red.txt')
    print(f"Calles {calles}")

    segundos, puntaje = _lector.leer_configuracion(r'../data/simulacion.txt')
    print(f"Segundos {segundos} y puntaje {puntaje}")

    trayectos = _lector.leer_trayectos(r'../data/trayectos.txt')

    _simulador = Simulador(puntaje, segundos, calles, trayectos)
    trayectos = _simulador.calcular_distancias() # Aca se calculan las distancias en cada trayecto, y se ponen en la primera posicion del arreglo

    _programacion = Programacion(trayectos, calles)
    print(f"Encolamiento de vehiculos {_programacion.cola_vehiculos}")

    print(f"Trayectos {trayectos}")

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

    _simulador.simular(programacion)

    # print(f'Archivo guardado en {_writer.create_program_report(programacion)}')

