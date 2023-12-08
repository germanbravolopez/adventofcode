def get_poker_strength(hand, jokers):
    char_cnt = {}
    for char in hand:
        char_cnt[char] = char_cnt.get(char, 0) + 1
    sorted_cnt = sorted(char_cnt.values(), reverse=True)
    print(sorted_cnt)
    if jokers:
        add_count_index_1 = 0
        for index, (char, cnt) in enumerate(char_cnt.items()):
            print(index, char, cnt)
            if index == 0 and char == "J":
                char_cnt[char] = 0
                if len(char_cnt) > 1:
                    add_count_index_1 += cnt
                else:
                    return 7
            elif index != 0 and char == "J":
                char_cnt[char] = 0
                char_cnt[list(char_cnt.keys())[0]] += cnt

        sorted_cnt = sorted(char_cnt.values(), reverse=True)
        sorted_cnt[0] += add_count_index_1


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

get_poker_strength('J233Q', 1)

'''
char_cnt = {'A': 3, '5': 2, 'J': 1}

add_count_index_1 = 0
print(len(char_cnt))
for index, (char, cnt) in enumerate(char_cnt.items()):
    print(char, cnt)
    if index == 0 and char == "J":
        char_cnt[char] = 0
        add_count_index_1 += cnt
    elif index != 0 and char == "J":
        char_cnt[char] = 0
        char_cnt[list(char_cnt.keys())[0]] += cnt

if add_count_index_1 > 0:
    char_cnt[list(char_cnt.keys())[1]] += add_count_index_1

# Print the updated dictionary
print(char_cnt)



hands = tuple((x[0], int(x[1])) for x in map(
    lambda x: x.strip().split(), open('day_07_input.txt').readlines()))

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'T', 'J', 'Q', 'K', 'A']


def score(hand, joker=None):
    jokers = 0 if joker is None else hand.count(joker)
    chars = sorted(
        (hand.count(x) for x in set(hand) if x != joker), reverse=True)
    chars = [5] if chars == [] else chars
    for (i, x) in enumerate(chars):
        n = min(5 - x, jokers)
        jokers -= n
        chars[i] += n
    s = ''.join(str(c) for c in chars).ljust(5, '0')
    for x in hand:
        s += str(0 if x == joker else cards.index(x) + 1).zfill(2)
    return int(s)


def total_winnings(hands, joker=None):
    flattened_data = sorted(hands, key=lambda x: score(x[0], joker))
    with open('debug_file_pass.txt', 'w') as file:
        for i in range(len(flattened_data)):
            file.write(str(flattened_data[i]) + '\n')
    return sum(map(lambda x: (x[0] + 1) * x[1][1],
                   enumerate(flattened_data)))


#print("1:", total_winnings(hands))
print("1:", total_winnings(hands, joker='J'))

'''