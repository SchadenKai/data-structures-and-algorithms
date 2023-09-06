## Graph search algorithms:
> The type of graph search algorithm is determined with the difference between the data structure applied to the frontier / search list. 

### Breadth-first search (BFS)
-  BFS uses a `Queue` data structure (FIFO) as the frontier.
-  The search / traversal of the graph is done through traversing through the shallowest nodes first / the neighbors of the current node.
-  Also known as level-order search since the search is done through levels / layers. 

### Depth-first search (DFS)
- DFS uses a `Stack` data structure (LIFO) as the frontier.
- The search / traversal of the graph is done through traversing through the deepest nodes first / the children of the current node.