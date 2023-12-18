def hash_algo(char: str, offset: int) -> int:
    return ((ord(char) + offset) * 17) % 256

def calculate_string(seq: str) -> int:
    value = 0
    for char in seq:
        value = hash_algo(char, value)
    return value

init_seq = open('inputs/day_15_input.txt', 'r').read().strip().split(',')

# Part 1
print(sum(calculate_string(seq) for seq in init_seq))

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

    # Perform operations
    current_label_stored = False
    for i, lens in enumerate(lens_boxes[box_key]):
        if lens[0] == op_label:
            if op_type:
                # Update focal_len for the stored len
                current_label_stored = True
                lens[1] = focal_len
            else:
                del lens_boxes[box_key][i]
    if op_type and not current_label_stored:
        # Add new item if it was not stored
        lens_boxes[box_key].append([op_label, focal_len])

# Calculate focusing power
result = 0
for box in lens_boxes:
    for i, lens in enumerate(lens_boxes[box]):
        result += int(lens[1]) * (i+1) * (box+1)
print(result)