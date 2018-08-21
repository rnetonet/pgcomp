visited = []

def bfs(graph, start):
    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0) # FIFO
        visited.append(node)

        for adjnode in graph[node]:
            if adjnode not in visited:
                queue.append(adjnode)


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }

    # [2, 0, 3, 1]
    bfs(graph, 2)
    print(visited)