# Read input from file
with open('input.txt', 'r') as file:
    list_1, list_2 = map(list, zip(*(map(int, line.strip().split()) for line in file)))