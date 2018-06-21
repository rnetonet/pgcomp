from sys import stdin, stdout

while True:
    data = stdin.readline()
    spot = data.index(' ')
    
    n_digits, n_digits_to_erase = int(data[0:spot]), int(data[spot:])
    if n_digits == 0: break
    
    n_output = n_digits - n_digits_to_erase
    
    number_lst = list(input())
    output = []

    start = 0
    for n in range(n_output, 0, -1):
        end = n_digits - (n - 1)
                
        view = number_lst[start:end]

        m = max(view)
        start = view.index(m) + start + 1

        output.append(m)
        n_output -= 1

    stdout.write(''.join(output) + '\n')