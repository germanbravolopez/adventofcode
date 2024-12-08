f = list(open('input.txt', 'r').read())
#print(f)
map_addr = {'^': (0,1),
            '>': (1,0),
            '<': (-1,0),
            'v': (0,-1)}

current_addr = (0,0)
list_addr = [current_addr]

for i in range(len(f)):
    current_addr = tuple(map(lambda i, j: i + j, current_addr, map_addr.get(f[i])))
    if not current_addr in list_addr:
        list_addr.append(current_addr)

print(len(list_addr))