def check_sets(set_list): # P1
    # Set cube counts
    red_count, green_count, blue_count = 12, 13, 14
    red_current, green_current, blue_current = 0, 0, 0

    for i in range(int(len(set_list)/2)):
        count = int(set_list[2*i])
        color = set_list[2*i+1]
        # count per color
        if color == "red":
            red_current += count
        elif color == "green":
            green_current += count
        elif color == "blue":
            blue_current += count
    return red_current <= red_count and green_current <= green_count and blue_current <= blue_count

def is_possible(game_line): # P1
    # Split the line into subsets
    game_sets = game_line.split(";")

    for game_set in game_sets:
        set_list = game_set.split()
        for i in range(len(set_list)):
            set_list[i] = set_list[i].replace(",", "")
        if not check_sets(set_list):
            return False
    return True

def get_min_cubes(set_list): # P2
    red, green, blue = 0, 0, 0

    for i in range(int(len(set_list)/2)):
        count = int(set_list[2*i])
        color = set_list[2*i+1]

        if color == "red":
            red += count
        elif color == "green":
            green += count
        elif color == "blue":
            blue += count
    return red, green, blue

def find_min_cubes(game_line): # P2
    game_sets = game_line.split(";")
    min_red_cube, min_green_cube, min_blue_cube = 0, 0, 0

    for game_set in game_sets:
        set_list = game_set.split()
        for i in range(len(set_list)):
            set_list[i] = set_list[i].replace(",", "")

        current_red, current_green, current_blue = get_min_cubes(set_list)

        if min_red_cube < current_red:
            min_red_cube = current_red
        if min_green_cube < current_green:
            min_green_cube = current_green
        if min_blue_cube < current_blue:
            min_blue_cube = current_blue

    return [min_red_cube, min_green_cube, min_blue_cube]

def solve_puzzle(input_lines):
    possible_game_ids = []
    sum_of_powers = 0

    for line in input_lines:
        parts = line.split(": ")
        game_id = parts[0].replace("Game ", "")
        game_contents = parts[1]

        # Part 1
        if is_possible(game_contents):
            possible_game_ids.append(int(game_id))

        # Part 2
        min_cubes = find_min_cubes(game_contents)
        power = min_cubes[0] * min_cubes[1] * min_cubes[2]
        sum_of_powers += power

    return sum(possible_game_ids), sum_of_powers

# Read input from file
with open('input.txt', 'r') as file:
    input_lines = file.readlines()

result_p1, result_p2 = solve_puzzle(input_lines)
print(result_p1, result_p2)
