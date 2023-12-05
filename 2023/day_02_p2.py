def get_min_cubes(set_list):
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

def find_min_cubes(game_line):
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

def calculate_sum_of_powers(input_lines):
    sum_of_powers = 0

    for line in input_lines:
        parts = line.split(": ")
        game_contents = parts[1]

        # Find the minimum set of cubes for each game
        min_cubes = find_min_cubes(game_contents)

        # Calculate the power of the minimum set for each game
        power = min_cubes[0] * min_cubes[1] * min_cubes[2]

        sum_of_powers += power

    return sum_of_powers

# Read input from file
with open('day_02_input.txt', 'r') as file:
    input_lines = file.readlines()

# Calculate the sum of the power of minimum sets for each game
result = calculate_sum_of_powers(input_lines)

print("The sum of the power of minimum sets is:", result)
