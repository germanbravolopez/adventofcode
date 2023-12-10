import math

D = open('inputs/day_08_input.txt').read().strip()
L = D.split('\n\n')
instr = L[0]
code_map = L[1].split('\n')
code_map_d = {i.split(' = ')[0]: i.split(' = ')[1] for i in code_map}


def search_map(current_key, finishing_key):
    n_moves = 0
    instr_idx = 0
    while not all(element in finishing_key for element in current_key):
        if instr[instr_idx] == 'L':
            for key_idx in range(len(current_key)):
                current_key[key_idx] = code_map_d.get(current_key[key_idx])[1:4]
            n_moves += 1
        else:
            for key_idx in range(len(current_key)):
                current_key[key_idx] = code_map_d.get(current_key[key_idx])[6:9]
            n_moves += 1
        if instr_idx >= len(instr) - 1:
            instr_idx = 0
        else:
            instr_idx += 1
    return n_moves

print(search_map(
    [node for node in code_map_d.keys() if node == 'AAA'],
    [node for node in code_map_d.keys() if node == 'ZZZ']))

starting_nodes = [node for node in code_map_d.keys() if node[2] == 'A']

solutions = []
for node in starting_nodes:
    solutions.append(search_map(
        [node],
        [node for node in code_map_d.keys() if node[2] == 'Z']))

print(math.lcm(*solutions))