pipes_map = {'|': ((-1,0),(1,0)),
             '-': ((0,-1),(0,1)),
             'L': ((-1,0),(0,1)),
             'J': ((-1,0),(0,-1)),
             '7': ((0,-1),(1,0)),
             'F': ((0,1),(1,0))
            }

board = list(open('day_10_input.txt'))
# get position of starting point
start_point = [(r, c) for r in range(140) for c in range(140)
                      if board[r][c] in 'S'][0]
pipes = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] in '|-LJ7F'}
pipes[start_point] = []
# create pipes connections
for pipe_pos in pipes.keys():
    if pipe_pos == start_point:
        match = '7' # small tweek
    else:
        match = board[pipe_pos[0]][pipe_pos[1]]
    pipes[pipe_pos].append((pipe_pos[0] + pipes_map.get(match)[0][0],
                            pipe_pos[1] + pipes_map.get(match)[0][1]))
    pipes[pipe_pos].append((pipe_pos[0] + pipes_map.get(match)[1][0],
                            pipe_pos[1] + pipes_map.get(match)[1][1]))
# algorithm matrix's
found = {pos: False for pos in pipes}
processed = {pos: False for pos in pipes}
parent = {pos: (-1, -1) for pos in pipes}

start_point = (37, 108)
finish_point = (36, 107)

def depth():
    q = [start_point]
    found[start_point] = True
    while q:
        v = q.pop()
        processed[v] = True

        for neighbor in pipes[v]:
            if not found[neighbor]:
                q.append(neighbor)
                found[neighbor] = True
                parent[neighbor] = v

def build_path():
    depth()
    path = [finish_point, ]
    p = finish_point
    while p != start_point:
        path.append(parent[p])
        p = parent[p]
    return path

path = build_path()
print(int(len(path)/2 + 0.5))
