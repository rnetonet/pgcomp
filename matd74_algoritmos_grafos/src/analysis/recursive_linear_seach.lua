function recursive_linear_search(a, i, v)
    if (a[i] == v) then
        return i
    else
        return recursive_linear_search(a, i - 1, v)
    end
end

print( recursive_linear_search({10, 20, 30, 40, 50}, 5, 20))