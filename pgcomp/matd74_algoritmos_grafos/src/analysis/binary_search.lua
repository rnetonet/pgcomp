-- binary_search.lua

function binary_search(arr, v, s, e)
    if (s > e) then
        return nil
    end

    middle = math.ceil((e + s) / 2)
    
    if arr[middle] == v then
        return middle
    elseif arr[middle] > v then
        return binary_search(arr, v, s, middle - 1)
    else
        return binary_search(arr, v, middle + 1, e)
    end
end

a = {10, 20, 30, 40, 50}
print(binary_search(a, 50, 1, #a))