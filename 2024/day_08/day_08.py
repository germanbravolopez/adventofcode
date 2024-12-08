# Read input from file
with open('input.txt', 'r') as file:
    reports = [list(map(int, line.strip().split())) for line in file]

print(-1)
print(-1)
