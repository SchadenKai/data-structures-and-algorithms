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
        # remove the node from the queue which will be the subject for the goal test
        # this eliminates to need to utilize further storage for the frontier 
        curr = search_queue.popleft()
        # if the current node is not in the searched list, add it to the queue / frontier 
        if curr not in searched:
            # goal test
            if curr == dest: 
                return("Found the target: " + curr + " in " + str(count) + " steps")
            # if goal test fails, add the neighboring nodes to the frontier / expand
            # add the failed nodes to the list of already searched nodes
            else: 
                search_queue += (graph[curr])
                searched.append(curr)
    # if the frontier is empty and the goal is not found, return not found
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
