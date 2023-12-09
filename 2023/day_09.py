def calculate_differences(sequence):
    return [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

def predict_next_value(sequence):
    differences = [sequence]

    for seq_depth in range(1, len(sequence)):
        differences.append(calculate_differences(differences[-1]))
        if all(diff == differences[-1][0] for diff in differences[-1]):
            for depth in range(len(differences) - 1, 0, -1):
                if depth != len(differences):
                    #print(differences[depth])
                    #print(differences[depth-1])
                    differences[depth-1].append(differences[depth-1][-1] + differences[depth][-1])
            #print(differences)
            return differences[0][-1]

def process_sequences_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    next_values = []
    for line in lines:
        # Assuming each line in the file contains a space-separated sequence of numbers
        sequence = [int(x) for x in line.strip().split()]
        next_values.append(predict_next_value(sequence))

        #print(f"Sequence: {sequence}, Predicted next value: {next_values[-1]}")
    print(sum(next_values))


file_path = 'day_09_input.txt'
process_sequences_from_file(file_path)
