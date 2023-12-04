# Set cube counts
red_count = 12
green_count = 13
blue_count = 14


def check_sets(set_list):
    current_red, current_green, current_blue = 0, 0, 0

    for i in range(int(len(set_list)/2)):
        count = int(set_list[2*i])
        color = set_list[2*i+1]

        if color == "red":
            current_red += count
        elif color == "green":
            current_green += count
        elif color == "blue":
            current_blue += count
    return current_red <= red_count and current_green <= green_count and current_blue <= blue_count


def is_possible(game_line):
    # Split the line into subsets
    game_sets = game_line.split(";")
    print(game_sets)

    for game_set in game_sets:
        set_list = game_set.split()
        for i in range(len(set_list)):
            set_list[i] = set_list[i].replace(",", "")

        if not check_sets(set_list):
            return False
    return True


def possible_games(input_lines):
    possible_game_ids = []

    for line in input_lines:
        parts = line.split(": ")

        game_id = parts[0].replace("Game ", "")
        game_contents = parts[1]

        # Check if the game is possible
        if is_possible(game_contents):
            possible_game_ids.append(int(game_id))
        else:
            print(f"Not possible: {line}")

    return possible_game_ids


# Read input from file
with open('day_02_input.txt', 'r') as file:
    input_lines = file.readlines()


# Find possible games
possible_ids = possible_games(input_lines)

# Calculate the sum of possible game IDs
result = sum(possible_ids)

print("The sum of IDs of possible games is:", result)
