local inspect = require('inspect')

function binary_sum(A, B)
    c = {}
    remainder = 0

    for j=#A,1,-1
    do
        sum = A[j] + B[j] + remainder
        remainder = 0
        if sum > 1 then
            sum = 1
            remainder = 0
        end

        c[j] = sum
    end

    return c
end

print( inspect(binary_sum({0, 1, 0, 1}, {0, 0, 0, 1})) )