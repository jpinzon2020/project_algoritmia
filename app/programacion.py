import math
import queue
class Programacion:

    def __init__(self, trayectos, calles, G):

        self.vertices_llegan = []
        self.cola_calles_finaliza_vertice = {}
        self.cola_calles_inicia_vertice = {}    
        self.cola_vehiculos = {}    
        self.cola_semaforos = {}    
        self.cola_calles_distancia = {}

        self.trayectos = trayectos
        self.calles = calles
        self.G = G
        self.list_all_streets = []
        self.convertir_a_columna()
        self.lista_calles()
        self.crear_encolamiento()
        
    def convertir_a_columna(self):
        self.vertices_llegan = [fila[1] for fila in self.calles]

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

    #Crea listado de calles
    def lista_calles(self):
        
        for street in self.trayectos: #n numero de calles en el prmer trayecto
            self.list_all_streets = [*street[2:], *self.list_all_streets]
        
        self.list_all_streets = list(dict.fromkeys(self.list_all_streets))
    
    #Crear un dict con la calle como valor
    #y la cantidad de vehículos encolados como valor
    # clave: nombre calle, valor: list(vehiculos encolados, peso calle)
    # 'calle1': [2, 5]
    def crear_encolamiento(self):
        
        indice_vehiculo = 0
        for calle in self.trayectos:
                
            if calle[2:][0] not in self.cola_vehiculos:
                vehiculos = []
                vehiculos.append(indice_vehiculo)
                self.cola_vehiculos[calle[2:][0]] = vehiculos
            else:
                self.cola_vehiculos[calle[2:][0]].append(indice_vehiculo)
            indice_vehiculo += 1
            #duracion_calle = self.encontrar_duracion_calle(calle[2:][0])    
        
        for calle_sin_cola in self.list_all_streets:
            if calle_sin_cola not in self.cola_vehiculos:
                vehiculos = []
                self.cola_vehiculos[calle_sin_cola] = vehiculos
        

        #n encolados en la calle
        #d distancia de la calle
        #m vertices al final de la calle
        #[calle1] list (n, d, m) = (n * d)/m
        for calle in self.cola_vehiculos:
            duracion_calle, cantidad_vertice, vertice_actual, cantidad_vertice_llega = self.encontrar_duracion_calle(calle)
            
            tiempo_semaforo = 0
            numero_vehiculos = len(self.cola_vehiculos[calle])
            #print(f"calle {calle} vehículos {n} vertices {cantidad_vertice} duración calle {duracion_calle}")
            if numero_vehiculos > 0:
                tiempo_semaforo = (numero_vehiculos * duracion_calle) / cantidad_vertice 

            self.cola_semaforos[calle] = tiempo_semaforo
            self.cola_calles_inicia_vertice[vertice_actual] = cantidad_vertice
            self.cola_calles_distancia[calle] = duracion_calle
            self.cola_calles_finaliza_vertice[vertice_actual] = cantidad_vertice_llega
        
        print("Semaforos", self.cola_semaforos)
        print("Intercceción calles inician", self.cola_calles_inicia_vertice)     
        print("Intercceción calles finalizan", self.cola_calles_finaliza_vertice)     
        print("Calles distancia", self.cola_calles_distancia)

    #Encontrar cantidad de vertices de la calle       
    def encontrar_duracion_calle(self, calle_buscada):
        
        for calle_actual in self.calles:
            if calle_buscada == calle_actual[2]:
                #vertices_llega = self.vertices_llegan.count(calle_actual[0])
                return calle_actual[3], self.bfs_editado(calle_actual[1]), calle_actual[1], 0     

        
    
