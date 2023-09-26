import networkx as nx
import matplotlib.pyplot as plt
import math

class Point:
	def __init__(self, id:str, x, y):
		self.id = id
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

def get_vizinhos(ponto:Point, visited, border, end_point:Point):
	for ed in edges:
		viz = None
		if (ed.p2.id == ponto.id) and (ed.p1.id not in visited): viz = ed.p1
		if (ed.p1.id == ponto.id) and (ed.p2.id not in visited): viz = ed.p2

		if viz != None:
			gn = ed.dist
			hn = calc_dist(end_point.x, end_point.y, viz.x, viz.y)
			viz.custo = gn + hn
			border.append(viz.id)



def get_lowest(arr):
	lowest:Point = None
	for el in arr:
		if lowest == None: lowest = points[el]
		elif points[el].custo < lowest.custo: lowest = points[el]

	return lowest

def calc_dist(x1:float, y1:float, x2:float, y2:float) -> int:
	return math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

def A_star(start_point:Point, end_point:Point):
	""" 
	adiciona start no visited
	act = start
	while True:
		se act == end: achado, para exescução
		colocar vizinhos do
	"""
	visited:list[str] = [] # lista de nós ja visitados
	border:list[str] = [] # lista de nós na fila de serem visitados
	
	border.append(start_point.id)

	while len(border) > 0:
		curr_point:Point = get_lowest(border)

		if curr_point.id == end_point.id:
			visited.append(curr_point.id)
			return visited

		border.remove(curr_point.id)
		visited.append(curr_point.id)

		# pega e calcula fn de vizinhos de current
		get_vizinhos(curr_point, visited, border, end_point)


#region extaindo dados
for nd in list(loaded.nodes):
	points[nd] = Point(nd, float(loaded.nodes[nd]['x']), -float(loaded.nodes[nd]['y']))

for p1, p2, data in list(loaded.edges):
	dist = calc_dist(points[p1].x, points[p1].y, points[p2].x, points[p2].y)
	edges.append(Edge(points[p1], points[p2], dist))

#endregion

caminho = A_star(points['n100'], points['n94'])

#region plot grafo
"""
# montando grafo
for eg in edges:
	graph.add_node(eg.p1.id, pos=(eg.p1.x, eg.p1.y))
	graph.add_node(eg.p2.id, pos=(eg.p2.x, eg.p2.y))
	graph.add_edge(eg.p1.id, eg.p2.id, weight=eg.dist)

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
"""
#endregion