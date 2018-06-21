from sys import stdin, stdout

while True:
    data = stdin.readline()
    spot = data.index(' ')
    
    n_digits, n_erase = int(data[0:spot]), int(data[spot:])
    if n_digits == 0: break
        
    number_lst = list(map(int, list(input())))

    output_length = n_digits - n_erase
    output = []

    for number in number_lst:
        while output and n_erase and number > output[-1]:
            output.pop()
            n_erase -= 1

        if len(output) < output_length: output.append(number)
            
    for number in output:
        print(number, end='')
    print()