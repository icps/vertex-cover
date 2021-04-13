#!/usr/bin/env python
# coding: utf-8

def edmonds_karp(graph, source, sink):
    max_flow  = 0
    res_graph = [[0 for i in range(len(graph))] for j in range(len(graph))]
    
    while True:
        path_flow, parents = BFS(graph, res_graph, source, sink)
        
        if path_flow == 0:
            break
            
        max_flow = max_flow + path_flow
        neighbor = sink
        
        while neighbor != source:    
            node                      = parents[neighbor]
            res_graph[node][neighbor] = res_graph[node][neighbor] + path_flow
            res_graph[neighbor][node] = res_graph[neighbor][node] - path_flow    
            neighbor                  = node
            
    return max_flow



def BFS(graph, res_graph, source, sink):
    parents         = [-1 for i in range(len(graph))]
    parents[source] = None
    
    cflow           = [0 for i in range(len(graph))]
    cflow[source]   = 5000    # infinity
    
    queue           = []
    queue.append(source)
    
    while queue:
        node = queue.pop(0)

        # "add" the inverse edge in graph if the residual graph has it
        neighbors = [e for e, i in enumerate(res_graph[node]) if i == -1]

        if len(neighbors) != 0:
            for v in neighbors:
                graph[node][v] = 1
                        
        for neighbor in graph[node]:

            if (graph[node][neighbor] - res_graph[node][neighbor] > 0) and parents[neighbor] == -1:
                parents[neighbor] = node
                cflow[neighbor]   = min(cflow[node], graph[node][neighbor] - res_graph[node][neighbor]) 

                if neighbor != sink:
                    queue.append(neighbor)

                else:
                    return cflow[sink], parents
            
    return 0, parents




def add_edge(graph, v1, v2, c):
    if v1 not in graph.keys():
        graph[v1] = {}
        
    graph[v1][v2] = c
    

def check_bipartite_side(graph):
    ### DFS to coloring
    visited = set()
    stack   = []
    color   = {k: False for k in graph.keys()}

    visited.add(1)
    stack.append(1)

    color[1] = False

    while stack:
        node  = stack.pop()

        for neighbor in graph[node]:
            if neighbor not in visited:

                stack.append(neighbor)
                visited.add(neighbor)

                color[neighbor] = not color[node]
                    
    return color
    
    
def add_flow_vertices(graph):    
    color         = check_bipartite_side(graph)
    
    source        = 0
    sink          = len(graph) + 1     
                        
    graph[source] = {}
    graph[sink]   = {}  
    
    for v, c in color.items():
        if c == False:
            add_edge(graph, source, v, 1)
            
        else:
            graph[v] = {}
            graph[v] = {sink: 1}

            
    
def bipartite_vertex_cover(graph, source, sink):
    # In any bipartite graph, the number of edges in a maximum matching equals 
    # the number of vertices in a minimum vertex cover (Konigs theorem)
    
    return edmonds_karp(graph, source, sink)


def main():
    
    V, E  = map(int, input().split(" "))
    
    if E > 0:

        graph = {}
        c     = 1

        for _ in range(int(E)):

            v1, v2 = map(int, input().split(" "))

            add_edge(graph, v1, v2, c)
            add_edge(graph, v2, v1, c)

        add_flow_vertices(graph)

        min_vertex_cover = bipartite_vertex_cover(graph, 0, V + 1)
        print(min_vertex_cover)
    
    else:
        print(0)
        

if __name__ == "__main__":
    main()



