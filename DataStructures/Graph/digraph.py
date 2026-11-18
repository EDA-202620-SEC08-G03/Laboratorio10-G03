from DataStructures.Map import map_linear_probing as lp 
from DataStructures.Graph import vertex as vtx
from DataStructures.List import array_list as al

def new_graph (order):
    
    graph = {
        'vertices': lp.new_map(order, 0.5),
        'num_edges': 0
    }

    return graph


def insert_vertex (my_graph, key_u, info_u):
    
    vertex_nuevo = vtx.new_vertex(key_u, info_u)
    my_graph["vertices"] = lp.put(my_graph["vertices"], key_u, vertex_nuevo)
    return my_graph


def add_edge (my_graph, key_u, key_v, weight=1.0):
    
    if not contains_vertex(my_graph, key_u):
        raise Exception("El vertice u no existe")
    
    if not contains_vertex(my_graph, key_v):
        raise Exception("El vertice v no existe")
    
    vertice_u = get_vertex(my_graph, key_u)

    if vtx.get_edge(vertice_u, key_v) is None:
        my_graph["num_edges"] += 1
        
    vtx.add_adjacent(vertice_u, key_v, weight)
    
    return my_graph
 
 
def contains_vertex (my_graph, key_u):
    
    return lp.contains(my_graph["vertices"], key_u) 
   
    
def size (my_graph):
    
    return my_graph["num_edges"]


def order (my_graph):
    
    return lp.size(my_graph["vertices"])


def degree (my_graph, key_u):
    
    if not contains_vertex(my_graph, key_u):
        raise Exception("El vertice no existe")
    
    vertice_u = get_vertex(my_graph, key_u)
    return vtx.degree(vertice_u)


def vertices (my_graph):
    
    return lp.key_set(my_graph["vertices"])


def adjacents (my_graph, key_u):
    
    if not contains_vertex(my_graph, key_u):
        raise Exception("El vertice no existe")
    
    vertice_u = get_vertex(my_graph, key_u)
    return lp.key_set(vtx.get_adjacents(vertice_u))


def edges_vertex (my_graph, key_u):
    
    if not contains_vertex(my_graph, key_u):
        raise Exception("El vertice no existe")
    
    vertice_u = get_vertex(my_graph, key_u)
    return lp.value_set(vtx.get_adjacents(vertice_u))


def get_vertex (my_graph, key_u):
    
    return lp.get(my_graph["vertices"], key_u)