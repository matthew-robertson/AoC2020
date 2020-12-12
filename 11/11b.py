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

def scan_slope(grid, x, y, dx, dy):
    tempx = x
    tempy = y
    while True:
        tempx += dx
        tempy += dy
        if tempx < 0 or tempy < 0 or tempx >= len(grid) or tempy >= len(grid[0]):
            return False
        if grid[tempx][tempy] == '#':
            return True
        elif grid[tempx][tempy] == 'L':
            return False

def count_neighbors(grid, x,y, target_char='#'):
    total = 0
    #left
    total += scan_slope(grid, x, y, -1, 0)
    total += scan_slope(grid, x, y, 1, 0)
    total += scan_slope(grid, x, y, 0, -1)
    total += scan_slope(grid, x, y, 0, 1)

    total += scan_slope(grid, x, y, -1, 1)
    total += scan_slope(grid, x, y, -1, -1)
    total += scan_slope(grid, x, y, 1, 1)
    total += scan_slope(grid, x, y, 1, -1)
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
    print("Checking generation %s" % gen)
    past_gen = copy.deepcopy(seating)
    for x in range(0, len(past_gen)):
        for y in range(0, len(past_gen[0])):
            if past_gen[x][y] == '.':
                continue
            nc = count_neighbors(past_gen, x, y)
            if nc == 0 and past_gen[x][y] == 'L':
                seating[x][y] = '#'
            elif nc >= 5 and past_gen[x][y] == '#':
                seating[x][y] = 'L'

print_grid(seating)
print('It took %s generations to stabilize at %s occupied seats' % (gen, count_seats(seating)))
