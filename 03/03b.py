grid = []
with open("input.txt", 'r') as  ins:
    rowCount = 0
    for line in ins:
        newLine = []
        for char in line:
            newLine.append(char == '#')
        grid.append(newLine)

def scanSlope(xMod, yMod):
    total = 0
    yToCheck = 0
    xToCheck = 0
    while yToCheck < len(grid):
        if grid[yToCheck][xToCheck % (len(grid[0])-1)]:
            total += 1

        xToCheck += xMod
        yToCheck += yMod 
    print ("On the slope %s, %s, you hit %s trees" % (xMod, yMod, total))
    return total

multTotal = scanSlope(1,1) * scanSlope(3,1) * scanSlope(5,1) * scanSlope(7,1) * scanSlope(1,2)
print("The answer is %s" % multTotal)
