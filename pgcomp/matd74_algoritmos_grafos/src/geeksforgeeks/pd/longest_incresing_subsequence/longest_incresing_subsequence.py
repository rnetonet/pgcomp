# longest_incresing_subsequence.py

def lis(ar):
    if len(ar) == 1: return 1

    _lis = [1 for i in range(len(ar))]

    for i in range(1, len(ar)):
        for j in range(i):
            if ar[j] < ar[i]:
                _lis[i] = max(_lis[i], _lis[j] + 1)

    return _lis[-1]
    
# Test cases Geeks for Geeks
cases = [
    [3, 10, 2, 1, 20],
    [3, 2],
    [50, 3, 10, 7, 40, 80]
]
outputs = [
    3,
    1,
    4
]

for index, case in enumerate(cases):
    print( lis(case), ' = ', outputs[index] )