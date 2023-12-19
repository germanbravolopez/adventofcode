def calculate_differences(sequence):
    return [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

def predict_next_value(sequence, next_value):
    differences = [sequence]

    for _ in range(1, len(sequence)):
        differences.append(calculate_differences(differences[-1]))
        if all(diff == differences[-1][0] for diff in differences[-1]):
            for depth in range(len(differences) - 1, 0, -1):
                if depth != len(differences):
                    if next_value:
                        differences[depth-1].append(differences[depth-1][-1] + differences[depth][-1])
                    else:
                        differences[depth-1].insert(0, differences[depth-1][0] - differences[depth][0])
            return differences[0][-1] if next_value else differences[0][0]

def process_sequences_from_file(file_path, next_value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    next_values = []
    for line in lines:
        sequence = [int(x) for x in line.strip().split()]
        next_values.append(predict_next_value(sequence, next_value))

        #print(f"Sequence: {sequence}, Predicted next value: {next_values[-1]}")
    print(sum(next_values))


file_path = 'input.txt'
process_sequences_from_file(file_path, True)
process_sequences_from_file(file_path, False)
