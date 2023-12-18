def hash_algo(char: str, offset: int) -> int:
    return ((ord(char) + offset) * 17) % 256

def calculate_string(seq: str) -> int:
    value = 0
    for char in seq:
        value = hash_algo(char, value)
    return value

init_seq = open('inputs/day_15_input.txt', 'r').read().strip().split(',')
debug = 1

# Part 1
print(sum(calculate_string(seq) for seq in init_seq))

init_seq = open('inputs/debug.txt', 'r').read().strip().split(',')
# Part 2
lens_boxes = {key: [] for key in range(256)}

for seq in init_seq:
    # Identify operation type
    if '-' in seq:
        op_type = 0
        op_label = seq[:-1]
    else:
        op_type = 1
        op_label, focal_len = seq.split('=')
    box_key = calculate_string(op_label)
    print(seq) if debug else None
    print(f'op_type: {op_type}\top_label: {op_label}\tbox_key: {box_key}') if debug else None

    for i, lens in enumerate(lens_boxes[box_key]):
        print(i, lens)
        if lens[0] == op_label:
            lens[1] = 0
    lens_boxes[box_key].append([op_label, focal_len])

print(lens_boxes)