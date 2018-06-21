# merge_sort.py

def merge(A, p, q, r):
    L = A[p:q]
    R = A[q:r]

    li = 0
    ji = 0

    L.append(float('inf'))
    R.append(float('inf'))

    for k in range(p, r):
        if L[li] <= R[ji]:
            A[k] = L[li]
            li += 1
        else:
            A[k] = R[ji]
            ji += 1
    
def merge_sort(A, p, r):
    if len(A[p:r]) < 2: return

    q = (p + r) // 2

    merge_sort(A, p, q)
    merge_sort(A, q, r)
    merge(A, p, q, r)

A = [3, 1, 4, 8, 7, 2, 9, 11]
merge_sort(A, 0, len(A))
print(A)