import networkx as nx
import matplotlib.pyplot as plt
import math
import eel
import matplotlib.image as mpimg
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)



locais = {
	"MCT": "n73",
	"INTUEL": "n72",
	"CEFE": "n66",
	"APLICACAO": "n69",
	"DP-COMUNICACAO": "n65",
	"CECA": "n58",
	"DP-ARTES": "n59",
	"DP-DESIGN": "n57",
	"CRECHE": "n63",
	"CEPV": "n60",
	"BIBL-CCH": "n56",
	"CESA": "n23",
	"CCH": "n24",
	"ANF-CCH": "n25",
	"DP-LETRAS": "n26",
	"DP-HIST": "n27",
	"DP-SOCIAIS": "n28",
	"XEROX": "n29",
	"PONTO-CCH": "n52",
	"CAPELA": "n21",
	"DP-FISICA": "n6",
	"DP-ESTATIST": "n7",
	"DP-GEO": "n3",
	"DP-COMP": "n4",
	"CA-COMP": "n8",
	"BIBL-CENTRAL": "n1",
	"SEBEC": "n33",
	"DP-QUIM": "n43",
	"CCA": "n2",
	"BANCOS": "n76",
	"RU": "n19",
	"CTU": "n38",
	"CCB": "n50",
	"DP-ANATOMIA": "n44",
	"PROGRAD": "n54",
}

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

loaded = nx.read_graphml('./Graph_map_Uel.graphml')
graph = nx.Graph()
points = {}
edges:list[Edge] = []

def GetName(nd):
	for k in locais:
		if locais[k] == nd:
			return k
	return ''

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

def MountGraph():
	# montando grafo
	for eg in edges:
		graph.add_node(eg.p1.id, pos=(eg.p1.x, eg.p1.y))
		graph.add_node(eg.p2.id, pos=(eg.p2.x, eg.p2.y))
		graph.add_edge(eg.p1.id, eg.p2.id, weight=3, color='black')

	# removendo nodes e edges inuteis
	graph.remove_node('n0')


def plotGraph():
	x, y = -536, -362
	img = mpimg.imread('./mapa_uel.webp')
	plt.imshow(img, extent=[x, x+1488, y+992, y])

	egs = graph.edges()
	colors = [graph[u][v]['color'] for u,v in egs]
	pos = nx.get_node_attributes(graph, 'pos')
	# nx.draw_networkx_edges(graph, pos=pos, width=3)
	nx.draw(graph, pos=pos, node_size=10, edge_color=colors, width=3)
	# nx.draw_networkx_labels(graph, pos=pos, font_size=9)
	nx.draw(graph)
	plt.show()

#region extaindo dados
for nd in list(loaded.nodes):
	points[nd] = Point(nd, float(loaded.nodes[nd]['x']), float(loaded.nodes[nd]['y']))

for p1, p2, data in list(loaded.edges):
	dist = calc_dist(points[p1].x, points[p1].y, points[p2].x, points[p2].y)
	edges.append(Edge(points[p1], points[p2], dist))
#endregion

#region eel
eel.init('web')

@eel.expose
def busca(de, para):
	n1 = locais[de]
	n2 = locais[para]
	caminho = A_star(points[n1], points[n2])

	print(caminho)

	MountGraph()

	# desenha o caminho
	aux = -1
	for i in range(len(caminho)-1, 0, -1):
		try:
			graph.remove_edge(caminho[i if aux == -1 else aux], caminho[i-1])
			graph.add_edge(caminho[i if aux == -1 else aux], caminho[i-1], color='red')
			aux = -1
		except:
			if aux == -1: aux = i
			pass

	plotGraph()

eel.start('index.html', mode='edge', app_mode=True)
#endregion


