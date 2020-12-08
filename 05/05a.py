def getPassFromInput(inputString):
    row = ''.join([str(int(bit == 'B')) for bit in inputString[:7]])
    column = ''.join([str(int(bit == 'R')) for bit in inputString[7:]])
    return {'row': row, 'column': column}

def getSeatIdFromPass(boarding_pass):
    return int(boarding_pass['row'], 2) * 8 + int(boarding_pass['column'], 2)

passes = []
with open('input.txt', 'r') as ins:
    for line in ins:
        line = line.strip()
        passes.append(getPassFromInput(line))

maximum = 0
for boarding_pass in passes:
    maximum = max(getSeatIdFromPass(boarding_pass), maximum)

print(maximum)
