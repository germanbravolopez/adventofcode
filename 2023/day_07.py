def get_poker_strength(hand):
    char_cnt = {}
    for char in hand:
        char_cnt[char] = char_cnt.get(char, 0) + 1
    sorted_cnt = sorted(char_cnt.values(), reverse=True)

    if sorted_cnt[0] == 5:
        return 7  # Five of a kind
    elif sorted_cnt[0] == 4 and sorted_cnt[1] == 1:
        return 6  # Four of a kind
    elif sorted_cnt[0] == 3 and sorted_cnt[1] == 2:
        return 5  # Full house
    elif sorted_cnt[0] == 3 and sorted_cnt[1] == 1 and sorted_cnt[2] == 1:
        return 4  # Three of a kind
    elif sorted_cnt[0] == 2 and sorted_cnt[1] == 2 and sorted_cnt[2] == 1:
        return 3  # Two pairs
    elif sorted_cnt[0] == 2 and sorted_cnt[1] == 1 and sorted_cnt[2] == 1 and sorted_cnt[3] == 1:
        return 2  # One pair
    else:
        return 1  # High card

def highest_card_sort_key(item):
    string, _, _ = item  # Unpack the list into string and random number
    char_order = "23456789TJQKA"
    return [char_order.index(c) for c in string]

# Read data file
f = open('day_07_input.txt').read().strip().split('\n')
# data = [hand, bid, strength]
data = [[sl[0], int(sl[1]), 0] for sl in [line.strip().split() for line in f]]

# Identify the type of hand
hands_strength_cnt = [0] * 7 # [1,2,3,4,5,6,7]
for i in range(len(data)):
    strength = get_poker_strength(data[i][0])
    data[i][2] = strength
    hands_strength_cnt[strength-1] += 1

# Sort all hands based on the identified strength
grouped_data = sorted(data, key=lambda x: x[2], reverse=False)

# Sort per highest card inside of each group
max_group = []
listed_grouped_data = [[grouped_data[i+sum(hands_strength_cnt[0:group_idx])] for i in range(hands_strength_cnt[group_idx])] for group_idx in range(len(hands_strength_cnt))]
sorted_grouped_data = [sorted(listed_grouped_data[group], key=highest_card_sort_key) for group in range(len(listed_grouped_data))]

# Flatten the list of sublists into a list of lists
flattened_data = [subsublist for sublist in sorted_grouped_data for subsublist in sublist]

# Calculate the result as a product of the index and the bid of that hand
result = 0
for i in range(len(flattened_data)):
    result += (i+1)*flattened_data[i][1]

#print(flattened_data)
print(result)
