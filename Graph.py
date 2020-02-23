# DataStructure used to represent a Graph
# Input: a List of Tuples representing a connection
class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Graph:
    def __init__(self, edges):
        #A list of tuples of chars
        self.edges = edges
        #Number of edges
        self.edges_number = self.countEdges(edges)
        #A set of char
        self.nodes = set()
        #Number of nodes
        self.nodes_number = self.countNodes(edges)
        #A set of Nodes(name, number)
        self.mapped_nodes = self.mapNode()
        #An array of sets, mapping each node number to the set of its neighborhood
        self.neighbors = self.makeNeighbors(edges)

    def countEdges(self, edges):
        return len(edges)

    #Return the number of unique nodes given a list of tuples
    #representing the edges of the graph
    #additionally for each new node found, keep track of that number and return it
    def countNodes(self, edges):
        number = 0
        for e in edges:
            if not(e[0] in self.nodes):
                self.nodes.add(e[0])
                number += 1
            if not(e[1] in self.nodes):
                self.nodes.add(e[1])
                number += 1
        return number

    #Returns a set of Nodes mapping each 'char' of a node to a number
    def mapNode(self):
        number = 0
        setMap = set()
        for n in self.nodes:
            setMap.add(Node(n, number))
            number += 1
        return setMap


    def makeNeighbors(self, edges):
        neighbors = [0]*self.nodes_number
        i = 0


        return neighbors


graph = Graph([('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')])
print(len(graph.neighbors))
