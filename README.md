# A Graph Data Structure in Python


The constructor of this class expects the following <b>input</b>:

An array of tuples of chars, for example:

```python
graph = Graph([('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'F')])
```

The limit of such class is that it only works for small graphs where the number of nodes does not exceeds the number of possible chars.



Each node is mapped to a number ( accessible with the getNumber('char') method ) and the main part of that class is the instance variable <b>neighbors</b>, where for a Graph g:

```python
g.neighbors[i]
```

is a set of the neighborhood of the Node which is mapped onto the number i.

