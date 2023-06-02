import collections

def bfs(graph,root): 
    visited, queue= set(), collections.deque([root])
    visited.add(root)

    while(queue):
        vertex=queue.popleft()
        print(str(vertex))
    
        for neighbour in graph[vertex]: 
            if neighbour not in visited:
                visited.add(neighbour) 
                queue.append(neighbour)

graph={'A':['B','C','F'],'B':['A','D'],'C':['A','E'],'D':['B','G'],
        'E':['C','G'],'F':['A','G'],'G':['D','E','F']} 
bfs(graph,'A')