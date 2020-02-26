# DataStructure to store a number-based Graph
# Author: Michele Cattaneo
# Version: 26.02.2020


class NumberGraph:
    def __init__(self, edges):
        self.edges_number = len(edges)
        self.edges = edges
        self.nodes = set()
        self.setNodes(edges)
        self.nodes_number = len(self.nodes)
        self.neighbors = self.setNeighborhood()

    # Array<Tuple<Int>> -> Nothing
    # Given the list of Edges, finds unique nodes and add them to self.nodes
    def setNodes(self, edges):
        for e in edges:
            if not (e[0] in self.nodes):
                self.nodes.add(e[0])
            if not (e[1] in self.nodes):
                self.nodes.add(e[1])

    # Nothing -> Array<Set<Int>>
    # Returns an array A of sets where Array[i] is the set of neighbors
    # of node i
    def setNeighborhood(self):
        neighbors = [0] * self.nodes_number

        for i in range(self.nodes_number):
            neighbors[i] = set()

        for e in self.edges:
            neighbors[e[0]].add(e[1])

        return neighbors

    # Int -> Set<Int>
    # Given a node, returns its neighborhood
    def getNeighbors(self, node):
        return self.neighbors[node]

    # Int -> Int
    # Given a node, returns its (out)Degree
    def getDegree(self, node):
        return len(self.neighbors[node])

    # Nothing -> Int[][]
    # Returns the adjecency matrix of the graph
    def getMatrix(self):
        matrix = [[0 for x in range(self.nodes_number)] for y in range(self.nodes_number)]
        for edge in self.edges:
            source = edge[0]
            dest = edge[1]
            matrix[source][dest] = 1
        return matrix

    # Int[][] -> Console
    # Given an adjecency  Matrix, prints it.
    def printMatrix(self, M):
        print("     ", end='')
        for i in range(len(M[0])):
            print(i," ",end='')
        print("")
        print("    ", end='')
        for k in range(len(M[0])):
            print("___", end='')
        print("")
        for row in range(len(M)):
            print(row," | ", end='')
            for col in range(len(M[0])):
                print(M[row][col]," ", end='')
            print("")

#TESTING

graph = NumberGraph([(0, 1), (0, 2), (1, 2), (1, 4), (4, 3), (3, 5)])
print(graph.getNeighbors(0))
print(graph.getNeighbors(1))
print(graph.getNeighbors(2))
print(graph.getNeighbors(3))
print(graph.getNeighbors(4))
print(graph.getNeighbors(5))
print(graph.edges)
graph.printMatrix(graph.getMatrix())