# largest_increasing_subsequence.py

def lis(seq):
    _lis = [1 for _ in range(len(seq))]
    
    for i in range(len(seq)):
        for j in range(i):
            if seq[j] <= seq[i]:
                _lis[i] = max(_lis[i], _lis[j] + 1)

    return max(_lis)

# 3
print( lis([3, 10, 2, 1, 20]) )

# 4
print( lis([50, 3, 10, 7, 40, 80]) )