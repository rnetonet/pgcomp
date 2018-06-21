# lis.py
def lis(seq):
    _lis = [1 for _ in seq]

    result = 0
    for i in range(len(seq)):
        for j in range(i):
            if seq[j] <= seq[i]:
                _lis[i] = max(_lis[i], _lis[j] + 1)
                result = max(result, _lis[i])
    return result

# 5
a = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
print( lis(a) )
