# Properties of the problem:
# - Points to install the radars
# - Each radar has a profit associated
# - Min distance between radars should be bigger than K

# number of test cases
num_cases = int(input())

while num_cases:
    num_radars, min_distance = list(map(int, input().split(' ')))
    positions = list(map(int, input().split(' ')))
    _profits = list(map(int, input().split(' ')))

    # spawn profits in relation to positions
    profits = [0] * max(max(positions) + 1, num_radars + 1)

    for index, position in enumerate(positions):
        profits[position] = max(profits[position], _profits[index])
    
    calculated_max = profits[0]
    for position, profit in enumerate(profits):
        print('KM', position, ' - ', profits)
        if position - min_distance >= 0:
            calculated_max = max(calculated_max, profit + profits[position - min_distance])
        else:
            calculated_max = max(calculated_max, profits[position])

        profits[position] = calculated_max
    
    print(profits)
    #print(calculated_max)

    num_cases -= 1