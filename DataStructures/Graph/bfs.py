from DataStructures.Map import map_linear_probing as mp
from DataStructures.Queue import queue
from DataStructures.Stack import stack
from DataStructures.List import array_list as al
from DataStructures.Graph import digraph as g


def bfs(graph, source):

    search = {
        "source": source,
        "visited": mp.new_map(g.order(graph), 0.5),
        "edge_to": mp.new_map(g.order(graph), 0.5)
    }

    bfs_vertex(search, graph, source)

    return search


def bfs_vertex(search, graph, source):

    q = queue.new_queue()

    mp.put(search["visited"], source, True)

    queue.enqueue(q, source)

    while not queue.is_empty(q):

        current = queue.dequeue(q)

        adjacents = g.adjacents(graph, current)

        for i in range(al.size(adjacents)):

            adjacent = al.get_element(adjacents, i)

            if not mp.contains(search["visited"], adjacent):

                mp.put(search["visited"], adjacent, True)

                mp.put(search["edge_to"], adjacent, current)

                queue.enqueue(q, adjacent)


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