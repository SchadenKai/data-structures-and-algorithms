from collections import deque

def breadth_first(graph, src, dest): 
    search_queue = deque()
    searched = []
    # use += operator for inserting elements, not the whole list
    search_queue += (graph[src])
    count = 0
    while search_queue:
        print(count)
        count+=1
        curr = search_queue.popleft()
        if curr not in searched:
            if curr == dest: 
                return("Found the target: " + curr)
            else: 
                search_queue += (graph[curr])
                searched.append(curr)
    return("Not found: " + dest)
        
dict = {}
dict["alice"] = ["bob", "kier", "tani"]
dict["bob"] = ["kairus"]
dict["kier"] = ["kairus"]
dict["tani"] = ["jhasmine"]
dict["kairus"] = []
dict["jhasmine"] = []

print(breadth_first(dict, "alice", "kairus"))
