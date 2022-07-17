from pathlib import Path
from objetos.interseccion import Interseccion


class Escritor:
    directorio = Path(__file__).parent

    def crear_reporte_desde_arreglos(self, ruta_archivo: str, contenido: list) -> str:
        vertices = len(contenido)

        with open(f'{ruta_archivo}', 'w') as f:
            f.write(f'{vertices}\n')

            i = 0
            for vertice in contenido:
                f.write(f'{i}\n')
                f.write(f'{len(vertice)}\n')

                for arista in vertice:
                    f.write(f'{arista[0]} {arista[1]}\n')

                i = i + 1

        f.close()

        return ruta_archivo

    def crear_reporte_desde_intersecciones(self, ruta_archivo: str, intersecciones: list[Interseccion]) -> str:
        cantidad_intersecciones = len(intersecciones)
        with open(f'{ruta_archivo}', 'w') as f:

            f.write(f'{cantidad_intersecciones}\n')

            i = 0
            for interseccion in intersecciones:
                f.write(f'{interseccion.interseccion}\n')

                semaforos_programados = interseccion.semaforos
                f.write(f'{len(semaforos_programados)}\n')
                for semaforo in semaforos_programados:
                    f.write(f'{semaforo.calle} {semaforo.duracion_luz_verde}\n')

                i = i + 1

        f.close()

        return ruta_archivo
