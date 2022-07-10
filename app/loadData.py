
from asyncore import read
from posixpath import split


def load_graph():
    G = [[]]
    try:
        red = open("c:/project_algorimia/data/red.txt", "r")
        red_line = red.readline()
        vertices, calles = red_line.split()
        indice_temp = 0
        while red_line != '':    
            red_line = red.readline()
            indice, vertice_asociado, nom_calle, peso = red_line.split()

            assoc = [int(vertice_asociado), int(peso), nom_calle]
            print(assoc)
            print("Indice a insertar", indice, "indice temp", indice_temp)

            if indice == indice_temp:
                G[int(indice)].extend(assoc)
            else:
                G[int(indice)].append(assoc)
                
            indice_temp = indice
                        
    except Exception as e: 
        print(repr(e))
        return None
    
    return G
