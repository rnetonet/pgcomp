MAX = 30

ncases = int(input())

for ncase in range(1, ncases + 1):
    print('Case #{}:'.format(ncase))

    nvertices, nedges = map(int, input().split(" "))
    
    adjacency = [[0 for _ in range(MAX)] for _ in range(MAX)]
    visited = [0 for _ in range(MAX)] 

    ordered = []
    total = 0

    def dfs(start):
        visited[start] = 1
        ordered.append(start)
        
        for i in range(nvertices):
            if adjacency[start][i]:
                if not visited[i]:
                    dfs(i)

    for _ in range(nedges):
        a, b = input().split(" ")
        
        ai = ord(a[0]) - 97
        bi = ord(b[0]) - 97

        adjacency[ai][bi] = 1
        adjacency[bi][ai] = 1

    for i in range(nvertices):
        if not visited[i]:
            total += 1
            dfs(i)
            ordered.sort()

            for j in range(len(ordered)):
                print("{},".format(chr(ordered[j] + 97)), end="")
            print()
        ordered = []
    
    print("{} connected components".format(total))
    print()
