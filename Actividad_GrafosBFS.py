"""
NOMBRE: Alexys Martin Coate Reyes
MATRÍCULA: A01746998

Instrucciones: Implementar DFS sobre un grafo que utilice matrices de adyacencia en lugar de listas ligadas
DFS (Depht First Search)
Referencia: https://www.geeksforgeeks.org/implementation-of-dfs-using-adjacency-matrix/
"""

class Grafo:

    #Inicializa un grafo con cierto número de nodos
    def __init__(self,size):
        self.size = size    #Indica el número de nodos
        self.matrizAdj = [[0 for nodoX in range(size)]
                       for nodoY in range(size)]   #Inicializa una matriz de 0 (sin conexiones)

    #Añade una ramificación unidireccional al grafo
    def unidirRama(self,nodo1,nodo2):
        self.matrizAdj[nodo1][nodo2] = 1

    #Añade una ramificación bidireccional al grafo
    def bidirRama(self,nodo1,nodo2):
        self.matrizAdj[nodo1][nodo2] = 1
        self.matrizAdj[nodo2][nodo1] = 1

    def DFS(self,nodoInicial,visitados):

        #Imprimir el nodo actual
        print(nodoInicial, end=' ')

        #Colocarl el nodoInicial como visitado
        visitados[nodoInicial] = True

        #Pasa por todos los nodos del grafo
        for nodo in range(self.size):
            #El nodo a comparar es el nodo en iteración
            nodoActual = self.matrizAdj[nodoInicial][nodo]
            #Pasa al siguiente nodo que tenga conexión con el nodo actual y no haya sisdo visitado
            #Primero se comparan los nodos menores y posteriormente los mayores
            if (nodoActual == 1 and not visitados[nodo]):
                #print(visitados)
                #Se llama al método DFS de manera recursiva
                self.DFS(nodo,visitados)

def ejemplo0():
    v = 5
    # Create the graph
    G = Grafo(v)
    G.bidirRama(0, 1)
    G.bidirRama(0, 2)
    G.bidirRama(0, 3)
    G.bidirRama(0, 4)
    # Visited vector to so that a vertex
    # is not visited more than once
    # Initializing the vector to false as no
    # vertex is visited at the beginning
    visited = [False] * v
    # Perform DFS
    G.DFS(0, visited);

def ejemplo1():
    tamaño = 4
    G = Grafo(tamaño)
    G.bidirRama(0, 1)
    G.bidirRama(0, 2)
    G.bidirRama(1, 3)
    visitados = [False] * tamaño
    G.DFS(3, visitados)

def ejemplo2():
    tamaño = 7
    G = Grafo(tamaño)
    G.bidirRama(0, 1)
    G.bidirRama(0, 2)
    G.bidirRama(0, 5)
    G.bidirRama(0, 6)
    G.bidirRama(1, 4)
    G.bidirRama(4, 6)
    G.bidirRama(6, 3)
    G.bidirRama(6, 5)
    visitados = [False] * tamaño
    G.DFS(0, visitados)

ejemplo0()
print()
ejemplo1()
print()
ejemplo2()