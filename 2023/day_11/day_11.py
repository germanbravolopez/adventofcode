# Read galaxy
initial_galaxy = []
num_galaxies = 0
for line in open('input.txt').readlines():
    row = []
    for char in line.strip():
        if char == "#":
            row.append(num_galaxies)
            num_galaxies += 1
        else:
            row.append(char)
    initial_galaxy.append(row)

exp_galaxy = []
for row in initial_galaxy:
    exp_galaxy.append(row)
    if all([char == "." for char in row]):
        exp_galaxy.append(row)

# Expand galaxy
galaxy = exp_galaxy
exp_galaxy = [[] for _ in galaxy]
for idy in range(len(galaxy[0])):
    for idx in range(len(galaxy)):
        exp_galaxy[idx].append(galaxy[idx][idy])
    if all([galaxy[idx][idy] == "." for idx in range(len(galaxy))]):
        for idx in range(len(galaxy)):
            exp_galaxy[idx].append(galaxy[idx][idy])

# Get galaxies positions
galaxies_positions = {exp_galaxy[idx][idy]: (idx, idy)
    for idx in range(len(exp_galaxy))
    for idy in range(len(exp_galaxy[0]))
    if exp_galaxy[idx][idy] != "."
}

pairs = [(i, j) for i in range(num_galaxies) for j in range(i, num_galaxies) if i < j]
# Manhattan distance

def manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return sum([abs(point1[0] - point2[0]), abs(point1[1] - point2[1])])

print(sum([manhattan_distance(galaxies_positions[i], galaxies_positions[j]) for i, j in pairs]))

# Part 2: use unexpanded galaxay
galaxies_positions = {
    initial_galaxy[idx][idy]: (idx, idy)
    for idx in range(len(initial_galaxy))
    for idy in range(len(initial_galaxy[0]))
    if initial_galaxy[idx][idy] != "."
}
pairs = [(i, j) for i in range(num_galaxies) for j in range(i, num_galaxies) if i < j]
empty_rows = [idx for idx, row in enumerate(initial_galaxy)
              if all([char == '.' for char in row])]

empty_cols = [idy for idy in range(len(initial_galaxy[0]))
              if all([initial_galaxy[idx][idy] == '.' for idx in range(len(initial_galaxy))])]

def get_extra_for_crossing_empties(point1, point2, empty_rows, empty_cols):
    extra = 0
    min_x, max_x = (point1[0], point2[0]) if point1[0] < point2[0] else (point2[0], point1[0])
    for row in empty_rows:
        if min_x < row < max_x:
            extra += 1_000_000 - 1

    min_y, max_y = (point1[1], point2[1]) if point1[1] < point2[1] else (point2[1], point1[1])
    for col in empty_cols:
        if min_y < col < max_y:
            extra += 1_000_000 - 1

    return extra

total = sum([
    (
        manhattan_distance(galaxies_positions[i], galaxies_positions[j])
        + get_extra_for_crossing_empties(galaxies_positions[i], galaxies_positions[j], empty_rows, empty_cols)
    )
    for i, j in pairs
])
print(total)