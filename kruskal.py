class Kruskal:

	def __init__(self):
		self.nodes = {}
		self.order = {}

	def prepare_data(self, node):
		self.nodes[node] = node
		self.order[node] = 0

	def find_node(self, node):
		if self.nodes[node] != node:
			self.nodes[node] = self.find_node(self.nodes[node])
		return self.nodes[node]

	def check_union(self, origin, arrival):
		origin_temp = self.find_node(origin)
		arrival_temp = self.find_node(arrival)
		if origin_temp != arrival_temp:
			if self.order[origin_temp] > self.order[arrival_temp]:
				self.nodes[arrival_temp] = origin_temp
			else:
				self.nodes[origin_temp] = arrival_temp
				if self.order[origin_temp] == self.order[arrival_temp]:
					self.order[arrival_temp] += 1

	def get_weight(self, edge):
		return edge[2]

	def apply_kruskal(self, edges, nodes):
		min_exp_tree = []
		# Recorrer los nodos y los insertamos en el diccionario previamente creado
		for node in nodes:
			self.prepare_data(node)
		# Ordenar las aristas de menor peso a mayor
		edges.sort(key=self.get_weight)
		# Recorrer las aristas ordenadas
		for edge in edges:
			origin, arrival, weight = edge
			if(self.find_node(origin) != self.find_node(arrival)):
				self.check_union(origin, arrival)
				min_exp_tree.append(edge)
		return min_exp_tree
