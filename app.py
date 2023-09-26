import networkx as nx
import matplotlib.pyplot as plt
import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.custo = 0

class Edge:
	def __init__(self, p1:Point, p2:Point, dist:float):
		self.p1 = p1
		self.p2 = p2
		self.dist = dist

"""
Point:
	0: x,
	1: y,
	2: custo pra prox passo

Edge:
	0: p1,
	1: p2,
	2: distancia dos pontos
"""

loaded = nx.read_graphml('./teste1.graphml')
graph = nx.Graph()
points = {}
edges:list[Edge] = []

def get_vizinhos(point):
	

def A_star(start_point, end_point):
	""" 
	adiciona start no visited
	act = start
	while True:
		se act == end: achado, para exescução
		colocar vizinhos do
	"""
	visited = [] # lista de nós ja visitados
	border = [] # lista de nós na fila de serem visitados
	
	visited.append(start_point)

	act_point = start_point
	act_point[2] = 0 + calc_dist(act_point[0], act_point[1], end_point[0], end_point[1])
	while True:
		if act_point == end_point: break

		# pega e calcula fn de vizinhos de act
		vizinhos = []
		for eg in edges:
			if eg.

		hn = calc_dist(act_point[0], act_point[1], end_point[0], end_point[1])

		fn = hn


def calc_dist(x1:float, y1:float, x2:float, y2:float) -> int:
	return math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))


#region extaindo dados
for nd in list(loaded.nodes):
	points[nd] = Point(float(loaded.nodes[nd]['x']), -float(loaded.nodes[nd]['y']))

for p1, p2, data in list(loaded.edges):
	dist = calc_dist(points[p1].x, points[p1].y, points[p2].x, points[p2].y)
	edges.append(Edge(p1, p2, dist))

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
