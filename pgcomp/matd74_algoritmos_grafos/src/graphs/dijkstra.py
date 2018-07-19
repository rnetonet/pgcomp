def dijkstra(graph, start, end):
    # Init costs
    costs = {start: 0}
    for vertex in graph:
        if vertex in costs: continue
        
        if vertex in graph[start]:
            costs[vertex] = graph[start][vertex]
        else:
            costs[vertex] = float("inf")

    # Init parents
    parents = {start: None}
    for vertex in graph:
        if vertex in parents: continue

        if vertex in graph[start]:
            parents[vertex] = start
    
    # Each node just needs to be processed one time
    processed = []

    # Calculating costs
    node = find_lowest_cost_node(costs, processed)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    # Reconstruct path
    path = [end]
    parent = parents[end]
    while parent:
        path.insert(0, parent)
        parent = parents[parent]

    return costs[end], path


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == "__main__":
    graph = {
        "start": {"A": 6, "B": 2},
        "A": {"end": 1},
        "B": {"A": 3, "end": 5},
        "end": {},
    }

    cost, path = dijkstra(graph, "start", "end")
    print("cost", cost)
    print("path", path)