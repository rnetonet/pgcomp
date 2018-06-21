def count(coins, n):
      table = [0 for k in range(n + 1)]
 
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
 
    return table[n]
 
# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
x = count(arr, m, n)
print (x)