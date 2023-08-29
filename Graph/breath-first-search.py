from collections import deque

def breadth_first(graph, src, dest): 
    # search queue = frontier 
    # this is the queue of nodes to be searched
    search_queue = deque()
    # this list represents the searched nodes 
    searched = []
    # use += operator for inserting elements, not the whole list
    # start with the initial state / source node
    search_queue += (graph[src])
    
    count = 0
    # while the queue is not empty, continue searching / looping
    while search_queue:
        
        # count the number of steps taken to find the target
        count+=1
        
        curr = search_queue.popleft()
        # if the current node is not in the searched list, add it to the queue / frontier 
        if curr not in searched:
            if curr == dest: 
                return("Found the target: " + curr + " in " + str(count) + " steps")
            else: 
                search_queue += (graph[curr])
                searched.append(curr)
    return("Not found: " + dest)
        
relationships = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["David", "Eve"],
    "Charlie": ["David"],
    "David": ["Eve"],
    "Eve": [],
    "Frank": ["Grace"],
    "Grace": []
}

print(breadth_first(relationships, "Alice", "David"))
