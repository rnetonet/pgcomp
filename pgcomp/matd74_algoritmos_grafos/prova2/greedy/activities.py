# Assume finish time sorted
def activites(start, finish):
    ids = []
    ids.append(0)
    
    last = 0

    for i in range(1, len(start)):
        if start[i] >= finish[last]:
            ids.append(i)
            last = i

    return ids

# 0 1 3 4
start = [1 , 3 , 0 , 5 , 8 , 5]
finish = [2 , 4 , 6 , 7 , 9 , 9]
print( activites(start, finish) )