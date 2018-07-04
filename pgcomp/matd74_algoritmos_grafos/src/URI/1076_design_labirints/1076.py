from collections import deque

ncases = int(input())

while ncases > 0:
    queue = deque()

    node = int(input())

    nvertices, nedges = map(int, input().split(" "))

    visited = {}
    adjacency = [[] for _ in range(nvertices)]

    for _ in range(nedges):
        a, b = map(int, input().split(" "))

        adjacency[a].append(b)
        adjacency[b].append(a)
    
    queue.append(node)
    visited[node] = True

    nlines = 0
    while queue:
        first = queue.popleft()
        for i in range(len(adjacency[first])):
            next = adjacency[first][i]
            if next not in visited:
                visited[next] = True
                queue.append(adjacency[first][i])
                nlines += 1
        nlines += 1
        
    print(nlines - 1)

    ncases -= 1
