from kruskal import Kruskal

# Declaramos las aristas y los nodes
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
edges = [
	['a', 'b', 7],
	['b', 'c', 8],
	['c', 'e', 5],
	['e', 'g', 9],
	['g', 'f', 11],
	['f', 'd', 6],
	['a', 'd', 5],
	['d', 'b', 9],
	['b', 'e', 7],
	['d', 'e', 15],
	['f', 'e', 8],
]
# Llamamos a la clase Kruskal
kruskal = Kruskal()
met = kruskal.apply_kruskal(edges, nodes)
print(f"El árbol obtenido es: {met}")
cost = sum(edge[2] for edge in met)
print(f"El costo total del árbol es: {cost}")