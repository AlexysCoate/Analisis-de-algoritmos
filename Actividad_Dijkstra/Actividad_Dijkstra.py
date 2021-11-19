"""
NOMBRE: Alexys Martín Coate Reyes
MARTÍCULA: a01746998

Código base extraido de: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ 
defaultDict: https://www.it-swarm-es.com/es/python/como-funciona-collections.defaultdict/973106122/#:~:text=defaultdict%20significa%20que%20si%20no,por%20el%20argumento%20de%20defaultdict.
"""
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys

class Graph():


	def __init__(self, vertices):
		self.V = vertices                                #Número de vertices o nodos
		self.graph = [[0 for column in range(vertices)]  #Matriz de adyacencias que tiene los diferentes uniones entre nodos
					for row in range(vertices)]

	def printSolution(self, dist):
		print ("Vertex \tDistance from Source")
		for node in range(self.V):
			print (node, "\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = float("inf")

		# Search not nearest vertex not in the
		# shortest path tree
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u

		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [float("inf")] * self.V      #Lista de distancias de tamaño "self.V" igual a infinito
		dist[src] = 0                       #El elemento donde incia el algoritmo tiene distancia 0
		sptSet = [False] * self.V           #Lista de visitados de tamaño "self.V" inicializada en falso (no visitado)

		for cout in range(self.V):      #Para cada nodo

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# x is always equal to src in first iteration
			x = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[x] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and \
				dist[y] > dist[x] + self.graph[x][y]:
						dist[y] = dist[x] + self.graph[x][y]

		self.printSolution(dist)

# Driver program
metro = Graph(28)
metro.graph = [ [0,	6,	0,	0,	0,	0,	0,	4,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [6,	0,	2,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	2,	0,	2,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	2,	0,	0,	3,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	2,	2,	0,	0,	3,	0,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	3,	3,	0,	3,	0,	0,	0,	0,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [4,	0,	0,	0,	0,	0,	0,	0,	0,	0,	7,	0,	0,	0,	0,	0,	0,	0,	0,	5,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	2,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	3,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	7,	1,	0,	0,	1,	0,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	2,	4,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	2,	0,	0,	0,	3,	0,	0,	0,	1,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	1,	6,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	0,	0,	0,	0,	1,	0,	0,	0,	6,	3,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	0,	0,	1,	0,	2,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	4,	0,	0,	0,	2,	0,	1,	0,	0,	0,	2,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0,	1,	0,	0,	0,	0,	0,	2,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	0,  6,	0,	0,	0,	0,	0,	0,	0,	0,	5,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	5,	0,	0,	0,	0,	0,	0,	6,	0,	0,	0,	0,	0,	3,	0,	0,	0,	3,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	3,	0,	2,	0,	0,	0,	4,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	0,	0,	0,	2,	0,	1,	2,	0,	0,	6,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	5,	0,	0,	1,	0,	1,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	1,	0,	0,	0,	0,	6],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	3,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	4,	0,	0,	0,	3,	0,	3,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	6,	0,	0,	0,	3,	0,	2],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	6,	0,	0,	2,	0],
            ]

metro.dijkstra(0)

# This code is contributed by Divyanshu Mehta
