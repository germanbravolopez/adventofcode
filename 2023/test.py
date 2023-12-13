d = open('inputs/day_13_input.txt', 'r').read().strip().split('\n\n')
#print(d[0].split('\n'))

def get_num_rows(pattern):
    print(pattern)
    pat = pattern.split('\n')
    prev_row = pat[0]
    for idy, row in enumerate(pat):
        if idy > 0:
            if row == prev_row:
                return idy
            prev_row = row

def get_num_cols(pattern):
    matrix = [x.split() for x in pattern.split('\n')]
    splitted_matrix = [[char for char in row[0]] for row in matrix]
    transp_matrix = list(map(list, zip(*splitted_matrix)))
    joined_matrix = [''.join(row) for row in transp_matrix]

    return get_num_rows('\n'.join(joined_matrix))


#print(get_num_rows(d[0]))
print(get_num_cols(d[0]))
#print(sum(100*get_num_rows(pattern)+get_num_cols(pattern) for pattern in d))