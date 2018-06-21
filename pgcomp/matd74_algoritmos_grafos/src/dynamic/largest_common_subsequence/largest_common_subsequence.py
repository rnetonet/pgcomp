# largest_common_subsequence.py

# Assume a as "master"
def largest_common_subsequence(a, b, b_index, a_index):
    if b_index == len(b): return 0

    for idx in range(a_index, len(a)):
        if b[b_index] == a[idx]:
            return 1 + largest_common_subsequence(a, b, b_index + 1, idx + 1)

    return largest_common_subsequence(a, b, b_index + 1, a_index)


X = "AGGTAB"
Y = "GXTXAYB"
print( largest_common_subsequence(X, Y, 0, 0) ) # 4 GeeksForGeeks