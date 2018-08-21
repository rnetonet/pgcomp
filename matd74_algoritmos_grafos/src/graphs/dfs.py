tin = []
tout = []

def dfs(graph, node):
    if node in tin:  return
    
    tin.append(node)

    for adjnode in graph[node]:
        if adjnode not in tin:
            dfs(graph, adjnode)

    tout.append(node)

if __name__ == "__main__":
    from datasets import simple_graph as graph

    # ['A', 'C', 'F', 'E', 'B', 'D']
    dfs(graph, "A")
    print('tin', tin)
    print('tout', tout)

    # [1, 2, 3, 5, 6, 4]
    graph_yt = {
        1: [2, 4],
        2: [3],
        3: [5, 6],
        4: [6],
        5: [1],
        6: []
    }
    
    tin, tout = [], []
    dfs(graph_yt, 1)
    print('tin', tin)
    print('tout', tout)