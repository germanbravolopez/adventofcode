f = list(open('inputs/day_03_input.txt', 'r').read())
print(f)
map_addr = {'^': (0,1),
            '>': (1,0),
            '<': (-1,0),
            'v': (0,-1)}
start_addr = (0,0)
list_addr = [start_addr]