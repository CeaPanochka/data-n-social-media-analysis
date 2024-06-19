"""
Генерация графа в модели Эрдёша-Реньи.
Вычисление средней степени вершины.
"""


from functools import reduce
import networkx as nx


n = 10
p = 0.3

# генерация графа
G = nx.erdos_renyi_graph(n, p)

# средняя степень вершины
a = reduce(lambda x, y: x + G.degree(y), G.nodes(), 0)
a_avg = float(a) / len(G.nodes())

# средняя степень вершины по формуле
calc_avg = (n-1)*p

# разница значений
div_a = calc_avg - a_avg

print("Средняя степень вершины фактическая: ", round(a_avg, 3))
print("Средняя степень вершины по формуле: ", round(calc_avg, 3))
print("Полученная разница значений: ", round(div_a, 3))
