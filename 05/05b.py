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

ordered_ids = [getSeatIdFromPass(boarding_pass) for boarding_pass in passes]
ordered_ids.sort()

full_set = set(range(ordered_ids[0], ordered_ids[-1]))
print(full_set - set(ordered_ids))
