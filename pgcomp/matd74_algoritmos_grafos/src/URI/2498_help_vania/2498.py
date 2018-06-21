#
# Properties
# Each book has a weight (w) and a degre of interest (v)
# Books will be transported in a bag with limited weight
# Objective: Try to maximize the total degree of interest
#
def knapsack(n, values, weights, capacity):
    matrix = [[0] * (capacity + 1) for i in range(n)]

    for i in range(n):
        for j in range(capacity + 1):
            if weights[i] <= j:
                matrix[i][j] = max(
                    matrix[i - 1][j],
                    matrix[i - 1][j - weights[i]] + values[i]
                )
            else:
                matrix[i][j] = matrix[i - 1][j]
        
    return matrix[i][j]

# Case number
case = 1

while True:
    # Get the number of books and the bag maximum capacity
    n_books = bag_capacity = None
    try:
        n_books, bag_capacity = map(int, input().split(' '))
    except:
        break

    # End of the entry, no more work to do
    if n_books == 0 and bag_capacity == 0:
        break

    # Constructing the lists of weights and interests
    weights = []
    interests = []

    counter = n_books
    while counter:
        # Read the book weight and its interest degree
        weight, interest = map(int, input().split(' '))

        # Add to the list
        weights.append(weight)
        interests.append(interest)

        # Update the loop control variable
        counter -= 1

    # Calculate case
    print('Caso {}: {}'.format(case, knapsack(n_books, interests, weights, bag_capacity)))

    case += 1
