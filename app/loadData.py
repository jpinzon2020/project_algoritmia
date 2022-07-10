
def load_graph():
    
    G = [[],[],[],[],[]]
    
    try:
        red = open("c:/project_algorimia/data/red.txt", "r")
        red_line = red.readline()
        vertices, calles = red_line.split()
        #G = [list] * int(vertices)
        count = 0

        while count < int(calles):
            red_line = red.readline()
            indice, vertice_asociado, nom_calle, peso = red_line.split()

            assoc_vertex = (int(vertice_asociado), int(peso), nom_calle)
            
            G[int(indice)].append(assoc_vertex)
            count = count + 1
                        
    except Exception as e: 
        print(repr(e))
        return None
    
    return G
