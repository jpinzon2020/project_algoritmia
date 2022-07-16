'''
Proyecto de algoritmia para Diplomado en Ciencias de la Computacion,
Institucion Universitaria Politecnico Grancolombiano. Julio de 2022

https://github.com/jpinzon2020/project_algoritmia/

Autores:
Ivan Rene Barrios
Jorge Alberto Pinzon
Jeisson Tadeo Diaz
Dannia Isabel Loaiza

Todos los derechos reservados
'''


import json
from pathlib import Path
from utilidades.lector import Lector
from utilidades.escritor import Escritor
from utilidades.codificador import Codificador
from utilidades.programador import Programador
from utilidades.simulador_objetos import SimuladorObjetos

from programacion import Programacion


_lector = Lector()
_escritor = Escritor()
_programador = Programador()
_directorio = Path(__file__).parent


def imprimir_calles_intersecciones_trayectos(calles: list, intersecciones: list, trayectos: list):
    calles_como_json = json.dumps(calles, indent=2, cls=Codificador)
    print(f'CALLES:\n{calles_como_json}')

    intersecciones_como_json = json.dumps(intersecciones, indent=2, cls=Codificador)
    print(f'INTERSECCIONES:\n{intersecciones_como_json}')

    trayectos_como_json = json.dumps(trayectos, indent=2, cls=Codificador)
    print(f'TRAYECTOS:\n{trayectos_como_json}')

def imprimir_programacion(intersecciones: list):
    intersecciones_como_json = json.dumps(intersecciones, indent=2, cls=Codificador)
    print(f'INTERSECCIONES:\n{intersecciones_como_json}')


if __name__ == '__main__':
    archivo_red = str((_directorio / r'../data/red.txt').resolve())
    archivo_trayectos = str((_directorio / r'../data/trayectos.txt').resolve())
    archivo_simulacion = str((_directorio / r'../data/simulacion.txt').resolve())

    segundos, puntaje = _lector.leer_configuracion(archivo_simulacion)
    print(f"SEGUNDOS {segundos}\nPUNTAJE {puntaje}")

    # Generamos el mapa vial, e imprimimos las calles, intersecciones y trayectos leidos de los archivos
    # para verificar que la lectura sea correcta
    mapa = _lector.leer_como_mapa_vial(archivo_calles=archivo_red,
                                       archivo_trayectos=archivo_trayectos)
    # imprimir_calles_intersecciones_trayectos(mapa.calles, mapa.intersecciones, mapa.trayectos)

    # Generamos la programacion, y la imprimimos para verificar que sea correcta
    intersecciones_programadas = _programador.programar_semaforos_por_tiempo_inicial(mapa_vial=mapa)
    # imprimir_programacion(intersecciones_programadas)

    simulador = SimuladorObjetos(mapa_vial=mapa, puntaje=puntaje, segundos=segundos)

    # Ejecutamos la simulacion con la programacion generada, la cual nos otorga un puntaje final
    puntaje_final = simulador.simular(intersecciones_programadas)








    #grafo = _lector.leer_como_grafo(archivo_red)
    # print(f"Grafo {grafo}")

    # Este es el listado de calles. Orden de las posiciones: desde donde sale, para donde va, nombre de la calle, distancia
    #calles = _lector.leer_como_lista_de_calles(archivo_red)
    #print(f"Calles {calles}")

    #trayectos = _lector.leer_trayectos(archivo_trayectos)

    #_simulador = Simulador(puntaje, segundos, calles, trayectos)
    #trayectos = _simulador.calcular_distancias() # Aca se calculan las distancias en cada trayecto, y se ponen en la primera posicion del arreglo

    #programacion = Programacion(trayectos, calles, grafo)
    #print(f"Encolamiento de vehiculos {programacion.cola_vehiculos}")

    #print(f"Trayectos {trayectos}")

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

