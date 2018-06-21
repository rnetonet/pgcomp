# insertion_sort_recursive.py

def insertion_sort_recursive(arr, n):
    # base
    if n <= 1: return
    
    insertion_sort_recursive(arr, n - 1)

    key = arr[n - 1]
    i = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1