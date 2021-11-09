"""
NOMBRE: Alexys Martín Coate Reyes
MARTÍCULA: a01746998

Código base extraido de: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
defaultDict: https://www.it-swarm-es.com/es/python/como-funciona-collections.defaultdict/973106122/#:~:text=defaultdict%20significa%20que%20si%20no,por%20el%20argumento%20de%20defaultdict.
"""

from collections import defaultdict
 

class Graph:
 
    # Constructor
    def __init__(self):
 
        # Crea un diccionario cuyas laves es el nodo del que salen las ramificaciones
        self.graph = defaultdict(list)
 
    # Crea una lista (si no hay) del nodo y añade el número del grafo al que tiene una unión
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Función de BFS
    def BFS(self, s):
 
        # Marca todos los nodos como no visitados
        visited = [False] * (max(self.graph) + 1)
 
        # Crea la cola del BFS
        queue = []
 
        # Añade a la cola el nodo inicial
        queue.append(s)
        visited[s] = True

        # Mientras la cola no esté vacia...
        while queue:
 
            #Saca el elemento de la pila y lo imprime (orden del recorrido)
            s = queue.pop(0)
            print (s, end = " ")
 
            #Para cada elemento dentro del grafo s
            for i in self.graph[s]:
                # Si no ha sido visitado entonces se agrega a la cola
                # Y si ya lo visitaron, entonces lo omite
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 

metro = Graph()
metro.addEdge(0,1)
metro.addEdge(0,7)
metro.addEdge(1,0)
metro.addEdge(1,2)
metro.addEdge(1,4)
metro.addEdge(2,1)
metro.addEdge(2,3)
metro.addEdge(2,4)
metro.addEdge(3,2)
metro.addEdge(3,5)
metro.addEdge(4,1)
metro.addEdge(4,2)
metro.addEdge(4,5)
metro.addEdge(4,8)
metro.addEdge(5,3)
metro.addEdge(5,4)
metro.addEdge(5,6)
metro.addEdge(5,12)
metro.addEdge(6,5)
metro.addEdge(6,13)
metro.addEdge(6,18)
metro.addEdge(7,0)
metro.addEdge(7,10)
metro.addEdge(7,19)
metro.addEdge(8,4)
metro.addEdge(8,9)
metro.addEdge(8,10)
metro.addEdge(9,8)
metro.addEdge(9,11)
metro.addEdge(9,12)
metro.addEdge(10,7)
metro.addEdge(10,8)
metro.addEdge(10,11)
metro.addEdge(10,14)
metro.addEdge(11,9)
metro.addEdge(11,10)
metro.addEdge(11,15)
metro.addEdge(11,16)
metro.addEdge(12,5)
metro.addEdge(12,9)
metro.addEdge(12,13)
metro.addEdge(12,17)
metro.addEdge(13,6)
metro.addEdge(13,12)
metro.addEdge(13,17)
metro.addEdge(13,18)
metro.addEdge(14,10)
metro.addEdge(14,15)
metro.addEdge(14,19)
metro.addEdge(14,20)
metro.addEdge(15,11)
metro.addEdge(15,14)
metro.addEdge(15,16)
metro.addEdge(15,21)
metro.addEdge(16,11)
metro.addEdge(16,15)
metro.addEdge(16,17)
metro.addEdge(16,21)
metro.addEdge(17,12)
metro.addEdge(17,13)
metro.addEdge(17,16)
metro.addEdge(17,22)
metro.addEdge(18,6)
metro.addEdge(18,13)
metro.addEdge(18,22)
metro.addEdge(19,7)
metro.addEdge(19,14)
metro.addEdge(19,20)
metro.addEdge(19,24)
metro.addEdge(20,14)
metro.addEdge(20,19)
metro.addEdge(20,21)
metro.addEdge(20,25)
metro.addEdge(21,15)
metro.addEdge(21,16)
metro.addEdge(21,20)
metro.addEdge(21,22)
metro.addEdge(21,23)
metro.addEdge(21,26)
metro.addEdge(22,17)
metro.addEdge(22,18)
metro.addEdge(22,21)
metro.addEdge(22,23)
metro.addEdge(23,21)
metro.addEdge(23,22)
metro.addEdge(23,27)
metro.addEdge(24,19)
metro.addEdge(24,25)
metro.addEdge(25,20)
metro.addEdge(25,21)
metro.addEdge(25,26)
metro.addEdge(26,21)
metro.addEdge(26,25)
metro.addEdge(26,27)
metro.addEdge(27,23)
metro.addEdge(27,26)

metro.BFS(0)
