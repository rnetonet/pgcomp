# two_days_in_london.py

times = [0.5, 0.5, 1, 2, 0.5]
ratings = [7, 6, 9, 9, 8]
capacity = 2

def two_days_in_london(times, ratings, capacity, i):
    if capacity == 0: return 0
    if len(times) == i: return 0
    
    if times[i] > capacity:
        return travel(times, ratings, capacity, i + 1)
    else:
        return max(
            travel(times, ratings, capacity, i + 1),
            ratings[i] + travel(times, ratings, capacity - times[i], i + 1)
        )

print( travel(times, ratings, capacity, i = 0) )