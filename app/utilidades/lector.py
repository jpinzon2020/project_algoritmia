from pathlib import Path
from objetos.calle import Calle
from objetos.interseccion import Interseccion
from objetos.mapa_vial import MapaVial
from objetos.vehiculo import Vehiculo


class Lector:
    directorio = Path(__file__).parent

# region LECTURA ARCHIVO DE RED

    '''
    La primera prueba llevo a leer como un grafo el archivo de red.
    Ello genera una matriz de adyacencia, que eventualmente se hizo dificil de analizar
    '''
    def leer_como_grafo(self, ruta_archivo: str) -> list:
        i = 0
        grafo = []

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

    '''
    En una segunda instancia, se evaluo la posibilidad de leer el archivo de red y generar una lista de calles.
    Si bien el analisis resulto mas rapido, hizo falta poder asociar calles e intersecciones facilmente
    '''
    def leer_como_lista_de_calles(self, ruta_archivo: str) -> list:
        i = 0
        calles = []

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

                i += 1

        f.close()

        return calles

# endregion

# region LECTURA ARCHIVO DE TRAYECTOS

    '''
    Una primera etapa de la lectura del archivo de Trayectos genera una lista con cada trayecto. Sin embargo, se dificulta
    asociar cada calle a una interseccion y calcular los tiempos de los semaforos en cada caso 
    '''
    def leer_trayectos(self, ruta_archivo: str) -> list:
        i = 0
        with open(f'{ruta_archivo}', 'r') as f:
            for linea in f:
                valores = linea.split()

                if i == 0:
                    # Inicializamos la cantidad de trayectos segun la cantidad dada en la primera posicion
                    trayectos = [None] * int(valores[0])
                else:
                    trayectos[i - 1] = valores

                i += 1
        f.close()

        return trayectos

# endregion

# region LECTURA DE ARCHIVOS FORMANDO UN MAPA VIAL

    '''
    Partiendo de los hallazgos encontrados con la lectura como una lista de calles (metodo leer_como_lista_de_calles),
    se identificaron potenciales usos directamente con la Orientacion a Objetos, para relacionar calles e intersecciones.
    En esta tercera etapa, se considero unir la lectura del archivo de Red y el de Trayectos como archivos directamente
    relacionados que generan un mapa vial 
    '''
    def leer_como_mapa_vial(self, archivo_calles: str, archivo_trayectos: str) -> MapaVial:
        print('Iniciando lectura como Mapa Vial')
        cantidad_intersecciones, intersecciones, cantidad_calles, calles = self.leer_como_objetos_calle_interseccion(archivo_calles)
        calles.sort(key=self.ordenar_por_nombre_calle)
        cantidad_vehiculos, vehiculos = self.leer_como_objeto_vehiculo_con_trayecto(archivo_trayectos)

        mapa_vial = MapaVial(cantidad_intersecciones=cantidad_intersecciones,
                             cantidad_calles=cantidad_calles,
                             cantidad_vehiculos=cantidad_vehiculos)
        mapa_vial.agregar_calles(calles)
        mapa_vial.agregar_intersecciones(intersecciones)
        mapa_vial.agregar_vehiculos(vehiculos)
        return mapa_vial

    @staticmethod
    def ordenar_por_nombre_calle(calle):
        return calle.nombre

    def leer_como_objetos_calle_interseccion(self, ruta_archivo: str):
        print(f'Iniciando lectura de Calles e Intersecciones en {ruta_archivo}')
        i = 0
        calles = []
        intersecciones = []

        with open(f'{ruta_archivo}', 'r') as f:
            for linea in f:
                valores = linea.split()

                if i == 0:
                    cantidad_intersecciones = int(valores[0])
                    intersecciones = [None] * cantidad_intersecciones

                    cantidad_calles = int(valores[1])
                else:
                    desde = int(valores[0])
                    hacia = int(valores[1])
                    nombre_calle = valores[2]
                    tiempo_para_recorrer = int(valores[3])

                    # Creamos la calle y la agregamos al listado
                    calle = Calle(nombre=nombre_calle, desde=desde, hacia=hacia, distancia=tiempo_para_recorrer)
                    calles.append(calle)

                    # Ya que una calle C va desde un punto A hacia un punto B, deducimos que en el punto B hay una calle
                    # entrante C. Asi, podemos crear u obtener la interseccion, si existe, y agregamos la calle entrante.
                    # Luego, agregamos la interseccion al listado de intersecciones en la posicion del numero de la
                    # interseccion; es decir, la interseccion 0 se agrega en la posicion 0, por ejemplo
                    if intersecciones[hacia]:
                        interseccion = intersecciones[hacia]
                    else:
                        interseccion = Interseccion(interseccion=hacia)

                    interseccion.agregar_calle_entrante(calle=nombre_calle)
                    intersecciones[hacia] = interseccion

                i += 1

        f.close()

        return cantidad_intersecciones, intersecciones, cantidad_calles, calles

    def leer_como_objeto_vehiculo_con_trayecto(self, ruta_archivo: str):
        print(f'Iniciando lectura de Vehiculos y Trayectos en {ruta_archivo}')
        i = 0
        vehiculos = []

        with open(f'{ruta_archivo}', 'r') as f:
            for linea in f:
                valores = linea.split()

                if i == 0:
                    cantidad_vehiculos = int(valores[0])
                else:

                    j = 0
                    while j < len(valores):
                        if j == 0:
                            vehiculo = Vehiculo(identificador=i - 1, cantidad_calles=int(valores[j]))
                        else:
                            vehiculo.agregar_calle_a_trayecto(valores[j])
                        j += 1
                    vehiculos.append(vehiculo)

                i += 1
        f.close()

        return cantidad_vehiculos, vehiculos

# endregion

# region LECTURA DEL ARCHIVO DE SIMULACION

    def leer_configuracion(self, ruta_archivo: str):
        print(f'Leyendo configuracion en {ruta_archivo}')
        with open(f'{ruta_archivo}', 'r') as f:
            segundos = int(f.readline())
            puntaje = int(f.readline())
            f.close()

        return segundos, puntaje

# endregion
