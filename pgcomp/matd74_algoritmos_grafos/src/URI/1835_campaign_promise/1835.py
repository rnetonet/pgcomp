cases = int(input())

def dfs(graph, node, visited):
    visited.add(node)

    if not node in graph:
        return None

    for node in graph[node] - visited:
        dfs(graph, node, visited)

n = 1
while cases:
    graph = {}

    spots = roads = None
    nspots = nroads = None

    line = input()
    if len(line.split(" ")) > 1:
        nspots, nroads = map(int, line.split(" "))
    else:
        nspots = int(line)
        nroads = int(input())

    spots = set(range(1, nspots + 1))

    for _ in range(nroads):
        x, y = map(int, input().split(" "))

        if x not in graph:
            graph[x] = set()
        if y not in graph:
            graph[y] = set()

        graph[x].add(y)
        graph[y].add(x)

    visited = set()

    dfs(graph, 1, visited)

    cont = 0
    for spot in spots:
        if spot not in visited:
            dfs(graph, spot, visited)
            cont += 1

    if not cont:
        print("Caso #{}: a promessa foi cumprida".format(n))
    else:
        print("Caso #{}: ainda falta(m) {} estrada(s)".format(n, cont))

    cases -= 1
    n += 1
