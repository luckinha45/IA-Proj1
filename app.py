import networkx as nx
import matplotlib.pyplot as plt
import math

def calc_dist(x1:float, y1:float, x2:float, y2:float) -> int:
	return math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

loaded = nx.read_graphml('./teste1.graphml')
graph = nx.Graph()
points = {}
edges = []

#region extaindo dados
for nd in list(loaded.nodes):
	points[nd] = (float(loaded.nodes[nd]['x']), -float(loaded.nodes[nd]['y']))

for n1, n2, data in list(loaded.edges):
	dist = str(calc_dist(points[n1][0], points[n1][1], points[n2][0], points[n2][1]))
	edges.append((n1, n2, dist))

#endregion

# montando grafo
for eg in edges:
	graph.add_node(eg[0], pos=(points[eg[0]][0], points[eg[0]][1]))
	graph.add_node(eg[1], pos=(points[eg[1]][0], points[eg[1]][1]))
	graph.add_edge(eg[0], eg[1], weight=eg[2])

# print(graph.nodes)

# removendo nodes e edges inuteis
graph.remove_node('n109')
graph.remove_edge('n30', 'n30')
graph.remove_edge('n39', 'n39')

pos = nx.get_node_attributes(graph, 'pos')


# nx.draw(graph, pos=pos, node_color='k')
nx.draw(graph, pos=pos, node_size=10)
nx.draw_networkx_labels(graph, pos=pos)
# labels = nx.get_edge_attributes(graph, 'weight')
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
nx.draw(graph)
plt.show()

# for nd in list(loaded.nodes):
# 	loaded.nodes[nd]['label'] = nd
# 	print(loaded.nodes[nd])
