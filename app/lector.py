from pathlib import Path


class Lector:
    directorio = Path(__file__).parent

    def leer_como_grafo(self, archivo):
        i = 0
        grafo = []

        ruta_archivo = (self.directorio / archivo).resolve()
        with open(f'{ruta_archivo}', 'r') as f:
            for linea in f:
                valores = linea.split()

                # Inicializamos el grafo segun la cantidad de vertices (intersecciones) que se encuentren
                if i == 0:
                    cant_intersecciones = int(valores[0])

                    for j in range(cant_intersecciones):
                        grafo.append([])
                else:
                    # Agregamos una calle que va desde una interseccion hacia otra, que tiene un nombre y un tiempo
                    # para recorrerla. Ademas inicializamos los tiempos asignados a las luces de los semaforos
                    desde = int(valores[0])
                    hacia = int(valores[1])
                    nombre_calle = valores[2]
                    tiempo_para_recorrer = int(valores[3])
                    luz_en_verde = 0
                    luz_en_rojo = 0

                    calle = [hacia, tiempo_para_recorrer, nombre_calle, luz_en_verde, luz_en_rojo]

                    calles = grafo[desde]
                    calles.append(calle)
                    grafo[desde] = calles

                i = i + 1

        f.close()

        return grafo

    def leer_como_lista_de_calles(self, archivo):
        i = 0
        calles = []

        ruta_archivo = (self.directorio / archivo).resolve()
        with open(f'{ruta_archivo}', 'r') as f:
            for linea in f:
                valores = linea.split()

                if i == 0:
                    calles = [None] * int(valores[1])
                else:
                    # Agregamos una calle que va desde una interseccion hacia otra, que tiene un nombre y un tiempo
                    # para recorrerla. Ademas inicializamos los tiempos asignados a las luces de los semaforos
                    desde = int(valores[0])
                    hacia = int(valores[1])
                    nombre_calle = valores[2]
                    tiempo_para_recorrer = int(valores[3])
                    luz_en_verde = 0
                    luz_en_rojo = 0

                    calle = [desde, hacia, nombre_calle, tiempo_para_recorrer, luz_en_verde, luz_en_rojo]

                    calles[i - 1] = calle

                i = i + 1

        f.close()

        return calles

    def leer_trayectos(self, archivo):
        i = 0
        ruta_archivo = (self.directorio / archivo).resolve()
        with open(f'{ruta_archivo}', 'r') as f:
            for linea in f:
                valores = linea.split()

                if i == 0:
                    # Inicializamos la cantidad de trayectos segun la cantidad dada en la primera posicion
                    trayectos = [None] * int(valores[0])
                else:
                    trayectos[i - 1] = valores

                i = i + 1
        f.close()

        return trayectos

    def leer_configuracion(self, archivo):
        ruta_archivo = (self.directorio / archivo).resolve()

        with open(f'{ruta_archivo}', 'r') as f:
            segundos = int(f.readline())
            puntaje = int(f.readline())
            f.close()

        return segundos, puntaje
