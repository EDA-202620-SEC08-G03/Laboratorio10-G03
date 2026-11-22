from DataStructures.Map import map_linear_probing as mp
from DataStructures.Stack import stack
from DataStructures.List import array_list as al
from DataStructures.Graph import digraph as g


def dfs(graph, source):

    search = {
        "source": source,
        "visited": mp.new_map(g.order(graph), 0.5),
        "edge_to": mp.new_map(g.order(graph), 0.5)
    }

    dfs_vertex(search, graph, source)

    return search


def dfs_vertex(search, graph, vertex):

    mp.put(search["visited"], vertex, True)

    adjacents = g.adjacents(graph, vertex)

    for i in range(al.size(adjacents)):

        adjacent = al.get_element(adjacents, i)

        if not mp.contains(search["visited"], adjacent):

            mp.put(search["edge_to"], adjacent, vertex)

            dfs_vertex(search, graph, adjacent)


def has_path_to(search, vertex):

    return mp.contains(search["visited"], vertex)


def path_to(search, vertex):

    if not has_path_to(search, vertex):
        return None

    path = stack.new_stack()

    current = vertex

    while current != search["source"]:

        stack.push(path, current)

        current = mp.get(search["edge_to"], current)

    stack.push(path, search["source"])

    return path