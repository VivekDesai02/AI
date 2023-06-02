graph={ 'A':set(['B','C','F']),
        'B':set(['A','D']),
        'C':set(['A','E']),
        'D':set(['B','G']),
        'E':set(['C','G']),
        'F':set(['A','G']),
        'G':set(['D','E','F'])}

def dfs(graph,start, visited=None):
    if visited is None: 
        visited=set()
    visited.add(start)
    print(start)

    for next in graph[start]-visited:
        dfs(graph,next,visited) 
    return visited

dfs(graph,'A')