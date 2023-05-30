graph = {'A':set(['B','C','F']),
         'B':set(['A','D']),
         'C':set(['A','E']),
         'D':set(['B','G']),
         'E':set(['C','G']),
         'F':set(['A','G']),
         'G':set(['D','E','F'])}

visited=set()


def dfs(visited,graph,node):
    if node not in visited:
        print("node =",node)
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            return
dfs(visited,graph, 'A')

