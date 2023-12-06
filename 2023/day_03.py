def is_valid(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols

def has_symbol_around(engine_schematic, row, col, rows, cols):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid(new_row, new_col, rows, cols) and engine_schematic[new_row][new_col] in "*+-=@#$%&/":
            return True
    return False

def get_part_number(engine_schematic, row, col):
    prev_idx, prev_found, next_idx, next_found = 0, 0, 0, 0

    for i in range(4):
        if not prev_found and not engine_schematic[row][col-i].isdigit():
            prev_idx = i - 1
            prev_found = 1
        if not next_found and not engine_schematic[row][col+i].isdigit():
            next_idx = i
            next_found = 1
    part_number_str = ""
    for i in range(-prev_idx, next_idx):
        part_number_str = part_number_str + engine_schematic[row][col+i]
    return part_number_str


def sum_of_part_numbers(engine_schematic, output_file):
    rows = len(engine_schematic)
    cols = len(engine_schematic[0]) - 1

    total_sum = 0
    with open(output_file, 'w') as file:
        for row in range(rows):
            col = 0
            while col < cols:
                if engine_schematic[row][col].isdigit():
                    tmp_part_number = get_part_number(engine_schematic, row, col)
                    if has_symbol_around(engine_schematic, row, col, rows, cols):
                        total_sum += int(tmp_part_number)
                        if not engine_schematic[row][col+1].isdigit():
                            col += 1
                        elif not engine_schematic[row][col+2].isdigit():
                            col += 2
                        else:
                            col += 3
                        # Debugging:
                        message = f"Row: {row}, Col: {col}, Part Number: {tmp_part_number}\n"
                        file.write(message)
                    else:
                        col += 1
                else:
                    col += 1

    return total_sum

# Read input from file
with open('day_03_input.txt', 'r') as file:
    engine_schematic = file.readlines()

result = sum_of_part_numbers(engine_schematic, 'day_03_output.txt')
print(result)
