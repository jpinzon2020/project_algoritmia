import json
from pathlib import Path
from utilidades.lector import Lector
from utilidades.escritor import Escritor
from utilidades.codificador import Codificador
from utilidades.programador import Programador

from programacion import Programacion


_lector = Lector()
_escritor = Escritor()
_directorio = Path(__file__).parent


def imprimir_calles_trayectos(calles: list, trayectos: list):
    calles_como_json = json.dumps(calles, indent=2, cls=Codificador)
    print(f'CALLES:\n{calles_como_json}')

    trayectos_como_json = json.dumps(trayectos, indent=2, cls=Codificador)
    print(f'TRAYECTOS:\n{trayectos_como_json}')


if __name__ == '__main__':
    archivo_red = str((_directorio / r'../data/red.txt').resolve())
    archivo_trayectos = str((_directorio / r'../data/trayectos.txt').resolve())
    archivo_simulacion = str((_directorio / r'../data/simulacion.txt').resolve())

    mapa = _lector.leer_como_mapa_vial(archivo_calles=archivo_red,
                                       archivo_trayectos=archivo_trayectos)
    # Para verificar que la lectura sea correcta, se imprimen las calles y trayectos leidos de los archivos
    # imprimir_calles_trayectos(mapa.calles, mapa.trayectos)

    segundos, puntaje = _lector.leer_configuracion(archivo_simulacion)
    print(f"SEGUNDOS {segundos}\nPUNTAJE {puntaje}")

    _programador = Programador(puntaje=puntaje, segundos=segundos)
    programacion_de_semaforos = _programador.simular(mapa)








    grafo = _lector.leer_como_grafo(archivo_red)
    # print(f"Grafo {grafo}")

    # Este es el listado de calles. Orden de las posiciones: desde donde sale, para donde va, nombre de la calle, distancia
    calles = _lector.leer_como_lista_de_calles(archivo_red)
    #print(f"Calles {calles}")

    trayectos = _lector.leer_trayectos(archivo_trayectos)

    #_simulador = Simulador(puntaje, segundos, calles, trayectos)
    #trayectos = _simulador.calcular_distancias() # Aca se calculan las distancias en cada trayecto, y se ponen en la primera posicion del arreglo

    #programacion = Programacion(trayectos, calles, grafo)
    print(f"Encolamiento de vehiculos {programacion.cola_vehiculos}")

    #print(f"Trayectos {trayectos}")

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

    #_simulador.simular(programacion)

    # print(f'Archivo guardado en {_writer.crear_reporte(programacion)}')

