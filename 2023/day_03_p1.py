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


def sum_of_part_numbers(engine_schematic):
    rows = len(engine_schematic)
    cols = len(engine_schematic[0]) - 1

    total_sum = 0
    for row in range(rows):
        col = 0
        while col < cols:
            if engine_schematic[row][col].isdigit():
                tmp_part_number = get_part_number(engine_schematic, row, col)
                if has_symbol_around(engine_schematic, row, col, rows, cols):
                    print(f"Row: {row}, Col: {col}, Part Number: {tmp_part_number}")
                    total_sum += int(tmp_part_number)
                    col += len(tmp_part_number) - 1
            col += 1

    return total_sum

# Read input from file
with open('day_03_input.txt', 'r') as file:
    engine_schematic = file.readlines()

result = sum_of_part_numbers(engine_schematic)
print(result)
