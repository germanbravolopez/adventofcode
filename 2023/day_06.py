def count_ways_to_beat_record(time, distance):
    ways_to_beat_record = 0
    for i in range(time):
        if (i*(time-i)) > distance:
            ways_to_beat_record += 1
    return ways_to_beat_record

def multiply_ways_to_beat_records(races):
    result = 1
    for race in races:
        time, distance = race
        ways_to_beat_record = count_ways_to_beat_record(time, distance)
        result *= ways_to_beat_record
    return result

# Input races
input_race_1 = [
    (60, 475),
    (94, 2138),
    (78, 1015),
    (82, 1650)
]

input_race_2 = [
    (60947882, 475213810151650)
]

# Calculate and print the result
result = multiply_ways_to_beat_records(input_race_1)
print("Race 1 is: ", result)

result = multiply_ways_to_beat_records(input_race_2)
print("Race 1 is: ", result)
