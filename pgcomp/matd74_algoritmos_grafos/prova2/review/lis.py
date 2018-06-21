# lis.py
def lis(seq):
    _lis = [1 for _ in seq]

    for i in range(len(seq)):
        for j in range(i):
            if seq[j] < seq[i]:
                _lis[i] = max(_lis[i], _lis[j] + 1)
    
    return _lis[len(seq) - 1]

# 5
a = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
print( lis(a) )
