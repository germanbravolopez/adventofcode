def calculate_calibration_sum(calibration_document):
    total_sum = 0

    for line in calibration_document:
        digits = [char for char in line if char.isdigit()]

        if len(digits) >= 2:
            calibration_value = int(digits[0] + digits[-1])
        else:
            calibration_value = int(digits[0] + digits[0])
        total_sum += calibration_value

    return total_sum

# Read input from file
with open('day_01_input.txt', 'r') as file:
    calibration_document = [line.strip() for line in file]

result = calculate_calibration_sum(calibration_document)
print("The sum of all calibration values is:", result)
