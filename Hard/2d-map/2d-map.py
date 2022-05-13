map = input().split(',')
   
def total_moves(map):
    pos = []
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col == 'P':
                pos.append((i, j))
    print(abs(pos[0][0] - pos[1][0]) + abs(pos[0][1] - pos[1][1]))

total_moves(map)