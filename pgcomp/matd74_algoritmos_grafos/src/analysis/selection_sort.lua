local inspect = require('inspect')

function selection_sort(A)
    for j=1, #A-1 do
        min = j
        for k=j+1, #A do
            if A[k] < A[min] then
                min = k
            end
        end
        aux = A[j]
        A[j] = A[min]
        A[min] = aux
    end

    return A
end

print( inspect(selection_sort({7, 3, 1, 2, 4})) )