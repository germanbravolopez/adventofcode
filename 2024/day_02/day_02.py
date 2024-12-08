# Condition 1: all increasing
def is_incr(levels):
    for i in range(len(levels)-1):
        if not(levels[i] < levels[i+1]):
            return False, i
    return True, None

# Condition 1: all decreasing
def is_decr(levels):
    for i in range(len(levels)-1):
        if not(levels[i] > levels[i+1]):
            return False, i
    return True, None

# Condition 1: complete
def is_cond_1(levels):
    return is_incr(levels)[0] or is_decr(levels)[0]

# Condition 2: distance between levels is in range(1,3)
def is_cond_2(levels):
    for i in range(len(levels)-1):
        if not(abs(levels[i] - levels[i+1]) <= 3):
            return False, i
    return True, None

# Part 1: checks both conditions
def part1(levels):
    return is_cond_1(levels) and is_cond_2(levels)[0]

def check_remove_possible_wrong_level(levels, idx):
    levels_temp_int_1 = levels.copy()
    levels_temp_int_2 = levels.copy()
    del levels[idx]
    del levels_temp_int_1[idx - 1]
    del levels_temp_int_2[idx + 1]
    if part1(levels):
        return True
    if part1(levels_temp_int_1):
        return True
    if part1(levels_temp_int_2):
        return True
    return False

# Part 2: check if by removing the index that make it unsafe, the report is fixed
def part2(levels):
    if part1(levels):
        return True
    else:
        levels_tmp_1 = levels.copy()
        levels_tmp_2 = levels.copy()
        if not(is_incr(levels)[0]):
            if check_remove_possible_wrong_level(levels, is_incr(levels)[1]):
                return True
        if not(is_decr(levels_tmp_1)[0]):
            if check_remove_possible_wrong_level(levels_tmp_1, is_decr(levels_tmp_1)[1]):
                return True
        if not(is_cond_2(levels_tmp_2)[0]):
            if check_remove_possible_wrong_level(levels_tmp_2, is_cond_2(levels_tmp_2)[1]):
                return True
        return False

# Read input from file
with open('input.txt', 'r') as file:
    reports = [list(map(int, line.strip().split())) for line in file]

print(sum(1 for report in reports if part1(report)))
print(sum(1 for report in reports if part2(report)))
