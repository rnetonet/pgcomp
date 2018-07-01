from collections import defaultdict, deque


def reverse(n):
    return int(str(n)[::-1])


ncases = int(input())

while ncases:
    start, goal = map(int, input().split(" "))

    visited = defaultdict(lambda: False)

    q = deque()
    q.append({"number": start, "step": 0})
    visited[0] = True

    while q:
        node = q.popleft()

        current_number = node["number"]
        current_step = node["step"]

        if current_number == goal:
            print(current_step)
            break

        next = current_number + 1
        if not visited[next]:
            visited[next] = True
            q.append({"number": next, "step": current_step + 1})

        reversed = reverse(current_number)
        if not visited[reversed]:
            visited[reversed] = True
            q.append({"number": reversed, "step": current_step + 1})

    ncases -= 1
