rows = 0
cols = 0

def is_valid(row, col):
    return 0 <= row < rows and 0 <= col < cols

def has_symbol_around(engine_schematic, row, col):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid(new_row, new_col) and engine_schematic[new_row][new_col] in "*+-=@#$%&/":
            return True

    return False

def sum_of_part_numbers(engine_schematic):
    rows = len(engine_schematic)
    cols = len(engine_schematic[0])

    total_sum = 0
    for row in range(rows):
        for col in range(cols):
            if engine_schematic[row][col].isdigit():
                tmp_part_number = get_full_part(row, col)
                if has_symbol_around(engine_schematic, row, col):
                    total_sum += int(engine_schematic[row][col])

    return total_sum

# Read input from file
with open('day_03_input.txt', 'r') as file:
    engine_schematic = file.readlines()

result = sum_of_part_numbers(engine_schematic)
print(result)
