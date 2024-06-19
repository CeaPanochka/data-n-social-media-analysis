"""
Вычисление меры центральности в собственных векторах.
Центральность для 8 узлов "горкой".
"""


import networkx as nx


G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
G.add_edges_from([(1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 7), (5, 6), (6, 7), (6, 8)])

print(list(map(lambda x: round(x, 2), nx.eigenvector_centrality(G).values())))
