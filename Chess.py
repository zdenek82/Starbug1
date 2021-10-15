size = 10
symbols = ['#',' ']
desk = []
for row in range(size):
    line = []
    for cell in range(size):
        i = (row+cell) % len(symbols)
        line.append(symbols[i])
    desk.append(''.join(line))
print('\n'.join(desk))