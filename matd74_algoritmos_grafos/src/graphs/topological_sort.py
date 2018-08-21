tin = []
tout = []
top = []

def topsort(graph, node):
    if node in tin: return
    
    tin.append(node)

    for adjnode in graph[node]:
        if adjnode not in tin:
            topsort(graph, adjnode)

    top.insert(0, node)
    tout.append(node)

if __name__ == "__main__":
    graph_gfg = {
        5: [2, 0],
        4: [0, 1],
        3: [1],
        2: [3],
        1: [],
        0: []
    }
    
    top, tin, tout = [], [], []
    for node in graph_gfg:
        topsort(graph_gfg, node)
    print('top', top)
    print('tin', tin)
    print('tout', tout)