from functools import partial

def get_poker_strength(hand, jokers):
    char_cnt = {}
    for char in hand:
        char_cnt[char] = char_cnt.get(char, 0) + 1
    sorted_cnt = sorted(char_cnt.values(), reverse=True)
    if jokers:
        add_count_jokers = 0
        for index, (char, cnt) in enumerate(char_cnt.items()):
            if char == "J":
                add_count_jokers += cnt
                char_cnt[char] = 0

            if index == 0 and len(char_cnt) == 1:
                return 7

        sorted_cnt = sorted(char_cnt.values(), reverse=True)
        sorted_cnt[0] += add_count_jokers

    if sorted_cnt[0] == 5:
        return 7  # Five of a kind
    elif sorted_cnt[0] == 4:
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

def highest_card_sort_key(item, char_order):
    string, _, _ = item  # Unpack the list into string and random number
    return [char_order.index(c) for c in string]

def solve_camel_cards(data, jokers, debug):
    # Identify the type of hand
    hands_strength_cnt = [0] * 7 # [1,2,3,4,5,6,7]
    for i in range(len(data)):
        strength = get_poker_strength(data[i][0], jokers)
        data[i][2] = strength
        hands_strength_cnt[strength-1] += 1

    # Sort all hands based on the identified strength
    grouped_data = sorted(data, key=lambda x: x[2], reverse=False)

    # Sort per highest card inside of each group
    listed_grouped_data = [[grouped_data[i+sum(hands_strength_cnt[0:group_idx])] for i in range(hands_strength_cnt[group_idx])] for group_idx in range(len(hands_strength_cnt))]
    if jokers:
        partial_sort_key = partial(highest_card_sort_key, char_order="J23456789TQKA")
    else:
        partial_sort_key = partial(highest_card_sort_key, char_order="23456789TJQKA")
    sorted_grouped_data = [sorted(listed_grouped_data[group], key=partial_sort_key) for group in range(len(listed_grouped_data))]

    # Flatten the list of sublists into a list of lists
    flattened_data = [subsublist for sublist in sorted_grouped_data for subsublist in sublist]

    if debug:
        if jokers: debug_file = 'debug_jokers.txt'
        else: debug_file = 'debug_no_jokers.txt'
        with open(debug_file, 'w') as file:
            for i in range(len(flattened_data)):
                file.write(str(tuple(flattened_data[i])) + '\n')


    # Calculate the result as a product of the index and the bid of that hand
    result = 0
    for i in range(len(flattened_data)):
        result += (i+1)*flattened_data[i][1]

    #print(flattened_data)
    if jokers:
        print("[P2] PASSED:" if result == 251003917 else "[P2] FAILED:", result)
    else:
        print("[P1] PASSED:" if result == 251029473 else "[P1] FAILED:", result)

# Read data file
f = open('day_07_input.txt').read().strip().split('\n')
# data = [hand, bid, strength]
data = [[sl[0], int(sl[1]), 0] for sl in [line.strip().split() for line in f]]

solve_camel_cards(data, jokers=0, debug=0)
solve_camel_cards(data, jokers=1, debug=0)
