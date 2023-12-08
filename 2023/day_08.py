D = open('day_08_input.txt').read().strip()
L = D.split('\n\n')
instr = L[0]
code_map = L[1].split('\n')
code_map_d = {i.split(' = ')[0]: i.split(' = ')[1] for i in code_map}

starting_key = 'AAA'
finishing_key = 'ZZZ'
current_key = starting_key

n_moves = 0

while current_key != finishing_key:
    for next_move in instr:
        if next_move == 'L':
            current_key = code_map_d.get(current_key)[1:4]
            n_moves += 1
        else:
            current_key = code_map_d.get(current_key)[6:9]
            n_moves += 1

print("P1 solved in:", n_moves, "moves")