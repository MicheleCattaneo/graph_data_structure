# DataStructure used to represent a Graph
# Input: a List of Tuples representing a connection
class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Graph:
    #Constructor:
    #Given an array of tuples of chars ( where a char represents a Node )
    #builds the graph
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
        self.neighbors = self.makeNeighbors()

    # Array<tuple<char>> -> Int
    # returns the number of edges for the given input
    def countEdges(self, edges):
        return len(edges)

    #Array<tuple<char>> -> Int
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

    # Nothing -> Set<Node>
    # Returns a set of Nodes(name, number)
    def mapNode(self):
        number = 0
        setMap = set()
        for n in self.nodes:
            setMap.add(Node(n, number))
            number += 1
        return setMap

    # Char -> Optional<Int>
    # Returns the number onto which the given char is mapped to
    # or an error if node is not present
    def getNumber(self, node):
        filtered = [n for n in self.mapped_nodes if n.name == node]
        if len(filtered) == 0:
            raise Exception('No Node found for: {}'.format(node))
        return filtered[0].number

    # Nothing -> Array<Set<Char>>
    # returns an array A, where A[i] is a set of all neighbors of the node
    # mapped onto i
    def makeNeighbors(self):
        neighbors = [0]*self.nodes_number

        for i in range(self.nodes_number):
            neighbors[i] = set()

        for e in self.edges:
            node_index = self.getNumber(e[0])
            neighbors[node_index].add(e[1])

        return neighbors

    # Char -> Set<Char>
    # Given a char representing a node, returns the set of its neighborhood
    def getNeighbors(self, node):
        return self.neighbors[self.getNumber(node)]

# Testing area
graph = Graph([('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')])
print(graph.getNeighbors('A'))
print(graph.getNeighbors('B'))
print(graph.getNeighbors('C'))
print(graph.getNeighbors('D'))
print(graph.getNeighbors('E'))
print(graph.getNeighbors('F'))
