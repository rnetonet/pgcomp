def lis(seq):
    _lis = [ 1 for _ in range(len(seq)) ]

    for i in range(len(seq)):
        for j in range(i):
            if seq[j] < seq[i]:
                _lis[i] = max(_lis[i], _lis[j] + 1)
    
    return _lis[-1]

# 4
print( lis([50, 3, 10, 7, 40, 80]) )