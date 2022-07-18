'''
Proyecto de algoritmia para Diplomado en Ciencias de la Computacion,
Institucion Universitaria Politecnico Grancolombiano.
Julio de 2022

https://github.com/jpinzon2020/project_algoritmia/

Autores:
Ivan Rene Barrios
Jorge Alberto Pinzon
Jeisson Tadeo Diaz
Dannia Isabel Loaiza

Todos los derechos reservados.
Cualquier tipo de copia o divulgacion no autorizada por todos los miembros tendra consecuencias legales
'''

import json
from pathlib import Path
from utilidades.lector import Lector
from utilidades.escritor import Escritor
from utilidades.codificador import Codificador
from utilidades.programador import Programador
from utilidades.simulador_objetos import SimuladorObjetos


_lector = Lector()
_escritor = Escritor()
_programador = Programador()
_directorio = Path(__file__).parent


def imprimir_calles_intersecciones_trayectos(calles: list, intersecciones: list, vehiculos: list):
    calles_como_json = json.dumps(calles, indent=2, cls=Codificador)
    print(f'CALLES:\n{calles_como_json}')

    intersecciones_como_json = json.dumps(intersecciones, indent=2, cls=Codificador)
    print(f'INTERSECCIONES:\n{intersecciones_como_json}')

    vehiculos_como_json = json.dumps(vehiculos, indent=2, cls=Codificador)
    print(f'VEHICULOS:\n{vehiculos_como_json}')


def imprimir_programacion(intersecciones: list):
    intersecciones_como_json = json.dumps(intersecciones, indent=2, cls=Codificador)
    print(f'INTERSECCIONES:\n{intersecciones_como_json}')


if __name__ == '__main__':
    archivo_red = str((_directorio / r'../data/red.txt').resolve())
    archivo_trayectos = str((_directorio / r'../data/trayectos.txt').resolve())
    archivo_simulacion = str((_directorio / r'../data/simulacion.txt').resolve())
    archivo_reporte = str((_directorio / r'../data/programacion1.txt').resolve())

    segundos, puntaje = _lector.leer_configuracion(archivo_simulacion)
    # print(f"SEGUNDOS {segundos}\nPUNTAJE {puntaje}")

    # Generamos el mapa vial, e imprimimos las calles, intersecciones y vehiculos generados de los archivos
    # para verificar que la lectura sea correcta
    mapa = _lector.leer_como_mapa_vial(archivo_calles=archivo_red,
                                       archivo_trayectos=archivo_trayectos)
    # imprimir_calles_intersecciones_trayectos(mapa.calles, mapa.intersecciones, mapa.vehiculos)

    # Generamos la programacion, y la imprimimos para verificar que sea correcta
    intersecciones_programadas = _programador.programar_semaforos_por_tiempo_inicial(mapa_vial=mapa)
    # imprimir_programacion(intersecciones_programadas)

    memoria = _lector.leer_como_mapa_de_calles(archivo_red)
    simulador = SimuladorObjetos(mapa_vial=mapa, puntaje=puntaje, segundos=segundos, memoria=memoria)

    # Ejecutamos la simulacion con la programacion generada, la cual nos otorga un puntaje final
    puntaje_final = simulador.simular(intersecciones_programadas)
    print(f'PUNTAJE FINAL: {puntaje_final}')

    _escritor.crear_reporte_desde_intersecciones(ruta_archivo=archivo_reporte, intersecciones=intersecciones_programadas)
