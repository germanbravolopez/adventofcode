def find_spelled_out_digit(line, start_index):
    spelled_out_digits = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    for end_index in range(start_index + 1, len(line) + 1):
        potential_digit = line[start_index:end_index].lower()
        numeric_representation = spelled_out_digits.get(potential_digit, None)

        if numeric_representation is not None:
            return numeric_representation, end_index

    return None, start_index + 1

def calculate_calibration_sum(calibration_document):
    total_numeric_sum, total_text_sum = 0, 0

    for line in calibration_document:
        # Part 1
        digits_numeric = [char for char in line if char.isdigit()]

        if len(digits_numeric) >= 2:
            calibration_value = int(digits_numeric[0] + digits_numeric[-1])
        else:
            calibration_value = int(digits_numeric[0] + digits_numeric[0])
        total_numeric_sum += calibration_value

        # Part 2
        i = 0
        while i < len(line):
            current_digit = line[i]

            if current_digit.isalpha():
                numeric_digit, end_index = find_spelled_out_digit(line, i)
                if numeric_digit is not None:
                    line = line[:i] + numeric_digit + line[end_index - 1:]
                    i += len(numeric_digit) - 1
            i += 1

        digits_text = [char for char in line if char.isnumeric()]

        if len(digits_text) >= 2:
            calibration_value = int(digits_text[0] + digits_text[-1])
        else:
            calibration_value = int(digits_text[0] + digits_text[0])
        total_text_sum += calibration_value

    return total_numeric_sum, total_text_sum

# Read input from file
with open('inputs/day_01_input.txt', 'r') as file:
    calibration_document = [line.strip() for line in file]

result_p1, result_p2 = calculate_calibration_sum(calibration_document)
print(result_p1, result_p2)
