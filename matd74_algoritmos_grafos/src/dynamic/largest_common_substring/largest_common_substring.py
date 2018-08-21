# largest_common_substring.py

def largest_common_substring(a, b, i):
    if i == min(len(a), len(b)) + 1: return 0
    
    m = 0

    for j in range(i, min(len(a), len(b))):
        if a[j] == b[j]: m += 1
    
    return max(m, largest_common_substring(a, b, i + 1))

print( largest_common_substring('fish', 'hish', 0) )
print( largest_common_substring('fish', 'vista', 0) )

# GeeksForGeeks
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
print( largest_common_substring(X, Y, 0) ) # 10