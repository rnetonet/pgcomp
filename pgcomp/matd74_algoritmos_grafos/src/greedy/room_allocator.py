# Already sorted by finish time
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]

def possible_activities(s, f):
    next_act = 0
    print(next_act)
    
    for i in range(len(f)):
        if s[i] >= f[next_act]:
            print(i)
            next_act = i
    
possible_activities(s, f)