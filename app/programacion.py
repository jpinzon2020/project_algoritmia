import math
import queue
class Programacion:

    def __init__(self, trayectos, calles, G):
        self.cola_vehiculos = {}    
        self.trayectos = trayectos
        self.calles = calles
        self.G = G
        self.crear_encolamiento()

    def bfs_editado(self, origen):
        Q = queue.Queue() 
        Q.put(origen) 
        cantidad_vertices = 0    
        
        while not Q.empty(): 
            u = Q.get() 
            for v in self.G[u]: 
                cantidad_vertices += 1
                Q.put(v[0])
            break
        return cantidad_vertices  

    #Crear un dict con la calle como valor
    #y la cantidad de vehículos encolados como valor
    # clave: nombre calle, valor: list(vehiculos encolados, peso calle)
    # 'calle1': [2, 5]
    def crear_encolamiento(self):

        for calle in self.trayectos:

            if calle[2:][0] not in self.cola_vehiculos:
                vehiculos = []
                vehiculo = 1
                vehiculos.append(vehiculo)
                self.cola_vehiculos[calle[2:][0]] = vehiculos
            else:
                vehiculo = max(self.cola_vehiculos[calle[2:][0]]) + 1
                self.cola_vehiculos[calle[2:][0]][0] = vehiculo

            #duracion_calle = self.encontrar_duracion_calle(calle[2:][0])    

        
        for calle in self.cola_vehiculos:
            duracion_calle, cantidad_vertice = self.encontrar_duracion_calle(calle)
            self.cola_vehiculos[calle].append(duracion_calle)
            self.cola_vehiculos[calle].append(cantidad_vertice)
        
    #Encontrar cantidad de vertices de la calle       
    def encontrar_duracion_calle(self, calle_buscada):
        
        for calle_actual in self.calles:
            if calle_buscada == calle_actual[2]:
                return calle_actual[3], self.bfs_editado(calle_actual[1])     

        
    
