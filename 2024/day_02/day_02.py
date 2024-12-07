# Condition 1: all increasing or all decreasing
def is_cond_1 (levels):
    increasing = True
    for i in range(len(levels)-1):
        if not(levels[i] < levels[i+1]):
            increasing = False
    if not(increasing):
        for i in range(len(levels)-1):
            if not(levels[i] > levels[i+1]):
                return False
        return True
    else:
        return True

# Condition 2: distance between levels is in range(1,3)
def is_cond_2 (levels):
    for i in range(len(levels)-1):
        if not(abs(levels[i] - levels[i+1]) <= 3):
            return False
    return True

# Read input from file
with open('input.txt', 'r') as file:
    reports = [list(map(int, line.strip().split())) for line in file]

print(sum(1 for report in reports if is_cond_1(report) and is_cond_2(report)))
