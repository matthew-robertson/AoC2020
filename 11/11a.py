import copy
import datetime

start = datetime.datetime.now()
seating = []
with open('input.txt', 'r') as ins:
    for line in ins:
        seating.append(list(line.strip()))

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def count_neighbors(grid, x,y, target_char='#'):
    total = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i == x and j == y):
                continue

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                continue
            total += grid[i][j] == target_char
    return total

def count_seats(grid):
    total = 0
    for row in grid:
        total += row.count('#')
    return total

past_gen = []
gen = 0
while not past_gen == seating:
    gen += 1
    past_gen = copy.deepcopy(seating)
    for x in range(0, len(past_gen)):
        for y in range(0, len(past_gen[0])):
            nc = count_neighbors(past_gen, x, y)
            if nc == 0 and past_gen[x][y] == 'L':
                seating[x][y] = '#'
            elif nc >= 4 and past_gen[x][y] == '#':
                seating[x][y] = 'L'

print_grid(seating)
print('It took %s generations to stabilize at %s occupied seats' % (gen, count_seats(seating)))
