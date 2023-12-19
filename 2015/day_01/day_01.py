f = list(open('input.txt', 'r').read())
floor, index, idx_basement, found = 0, 0, 0, 0
for item in f:
    index += 1
    if not found and floor == -1:
        found = 1
        idx_basement = index - 1
    if item == '(':
        floor += 1
    else:
        floor -= 1
print(floor)
print(idx_basement)
