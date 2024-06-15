"""
Реализация алгоритма Дейкстры.
"""


import networkx as nx
import random
import sys


MAX_VALUE = sys.maxsize


def dijkstras_algorithm(g, start):
    """
    Алгоритм Дейкстры
    """
    unvisited_nodes = list(g.nodes)
 
    shortest_path = {node: MAX_VALUE for node in unvisited_nodes}
    shortest_path[start] = 0

    previous_nodes = {}
    
    while unvisited_nodes:

        unvisited_path = dict(filter(lambda item: item[0] in unvisited_nodes, shortest_path.items()))
        current_node = min(unvisited_path, key=unvisited_path.get)
                
        neighbors = list(g.neighbors(current_node))
        for neighbor in neighbors:
            t_cost = shortest_path[current_node] + g[current_node][neighbor]['weight']
            if t_cost < shortest_path[neighbor]:
                shortest_path[neighbor] = t_cost
                previous_nodes[neighbor] = current_node
 
        unvisited_nodes.remove(current_node)
    
    return previous_nodes, shortest_path


def print_shortest_path(previous_nodes, start, target):
    """
    Вывод кратчайшего пути
    """
    path = []
    node = target
    
    while node != start:
        path.append(str(node))
        node = previous_nodes[node]

    path.append(str(start))

    print(f"Shortest path: {'-'.join(list(reversed(path)))}")


# генерируем случайный граф
count_node = 50
count_edges = count_node*(count_node-1)/2
G = nx.dense_gnm_random_graph(count_node, count_edges)
attrs = {x: random.randint(2, 10) for x in list(G.edges)}
nx.set_edge_attributes(G, attrs, 'weight')


# применяем алгоритм дейкстры
start, target = 0, random.randint(1, count_node)
previous_nodes, shortest_path = dijkstras_algorithm(G, start)
print(f'Length is {shortest_path[target]}')
print_shortest_path(previous_nodes, start, target)

# сравниваем с nx
print(nx.dijkstra_path(G, start, target), nx.dijkstra_path_length(G, start, target))
