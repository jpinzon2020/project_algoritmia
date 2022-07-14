import queue 

class Programacion:


    def __init__(self, trayectos, calles):
        self.cola_vehiculos = {}    
        self.trayectos = trayectos
        self.calles = calles
        self.crear_encolamiento()

    #Crear un dict con la calle como valor
    #y la cantidad de vehículos encolados como valor
    # clave: nombre calle, valor: list(vehiculos encolados, peso calle)
    # 'calle1': [2, 5]
    def crear_encolamiento(self):
        #list_all_streets = []
        
        #for street in journeys: #n numero de calles en el prmer trayecto
        #    list_all_streets = [*street[1:], *list_all_streets]
        
        #list_all_streets = list(dict.fromkeys(list_all_streets))

        #for nom_calles in calles:
        #    print(nom_calles[0].index("calle10"))

        #return list_all_streets
        
        for calle in self.trayectos:

            if calle[2:][0] not in self.cola_vehiculos:
                vehiculos = []
                vehiculo = 1
                vehiculos.append(vehiculo)
                self.cola_vehiculos[calle[2:][0]] = vehiculos
            else:
                vehiculo = max(self.cola_vehiculos[calle[2:][0]]) + 1
                self.cola_vehiculos[calle[2:][0]][0] = vehiculo

            duracion_calle = self.encontrar_duracion_calle(calle[2:][0])    

        
        for calle in self.cola_vehiculos:
            duracion_calle = self.encontrar_duracion_calle(calle)
            self.cola_vehiculos[calle].append(duracion_calle)
        
    #Retornar la duración de una calle        
    def encontrar_duracion_calle(self, calle_buscada):
        
        for calle_actual in self.calles:
            
            if calle_buscada == calle_actual[2]:
                return calle_actual[3]