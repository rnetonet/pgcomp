-- insertion_sort_recursive.lua

function insertion_sort_recursive(A, n)
    if n == 1 then
        return
    end

    insertion_sort_recursive(A, n - 1)
    
    key = A[n]
    i = n - 1

    while i > 0 and A[i] > key do
        A[i + 1] = A[i]
        i = i - 1
    end

    A[i + 1] = key
end

A = {10, 1, 2, 7, 9, 11, 3}
insertion_sort_recursive(A, #A)

for k, v in pairs(A) do
    print(v)
end