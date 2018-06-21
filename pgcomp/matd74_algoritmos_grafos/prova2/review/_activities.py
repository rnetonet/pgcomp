def activities(start, finish):
    answer = []
    answer.append(0)
    last = 0

    for i in range(1, len(finish)):
        if start[i] >= finish[last]:
            answer.append(i)
            last = i
    
    return answer

# 0 1 3 4
start = [1 , 3 , 0 , 5 , 8 , 5]
finish = [2 , 4 , 6 , 7 , 9 , 9]
print( activities(start, finish) )