# Read input from file
with open('input.txt', 'r') as file:
    list_1, list_2 = map(list, zip(*(map(int, line.strip().split()) for line in file)))

# Sort both lists
list_1.sort(reverse=True)
list_2.sort(reverse=True)

print(sum([abs(list_1[i] - list_2[i]) for i in range(len(list_1))]))

print(sum([list_1[i] * list_2.count(list_1[i]) for i in range(len(list_1))]))