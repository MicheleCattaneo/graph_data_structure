# A Graph Data Structure in Python

**Graph.py**: A Char-based graph

**NumberGraph.py**: A Number-based graph

These are the expected inputs for their constructors:

```python
# For Char-based graph ( Graph.py )
graph = Graph([('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'F')])

# For Number-based graph ( NumberGraph.py )
graph = NumberGraph([(0, 1), (0, 2), (1, 2), (1, 4), (4, 3), (3, 5)])

```



For the Graph.py class each node is mapped to a number ( accessible with the getNumber('char') method ) and the main part of that class is the instance variable <b>neighbors</b>, where for a Graph g:

```python
g.neighbors[i]
```

is a set of the neighborhood of the Node which is mapped onto the number i.

The class NumberGraph.py is similar, the only real difference is that is working directly with numbers without a mapping char <-> Int

