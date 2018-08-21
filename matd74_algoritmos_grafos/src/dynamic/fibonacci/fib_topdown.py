# fib.py
cache = {}

def fib(n):
    if n not in cache:
        if n <= 1: cache[n] = n
        else: cache[n] = fib(n-1) + fib(n-2)
    
    return cache[n]

print( fib(30) )