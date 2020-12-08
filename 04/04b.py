ids = []
with open('input.txt', 'r') as ins:
  parsed_line = {}
  for line in ins:
    if len(line.strip()) == 0:
        ids.append(parsed_line)
        parsed_line = {}
    else:
        pairs = line.split(" ")
        for pair in pairs:
            vals = pair.split(":")
            parsed_line[vals[0]] = vals[1].strip()
    ids.append(parsed_line)

totals = [0,0,0,0,0,0,0]
def is_valid(passport):
    to_check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not all(field in passport.keys() for field in to_check):
        return False

    validBirth = isValidYear(passport['byr'], 1920, 2002)
    validIssue = isValidYear(passport['iyr'], 2010, 2020)
    validExpiration = isValidYear(passport['eyr'], 2020, 2030)

    validHeight = isValidHeight(passport)
    validHair = isValidHair(passport)

    ecl = passport['ecl']
    validEye = ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    validPid = len(passport['pid']) == 9 and passport['pid'].isnumeric()

    totals[0] += validBirth
    totals[1] += validIssue
    totals[2] += validExpiration
    totals[3] += validHeight
    totals[4] += validHair
    totals[5] += validEye
    totals[6] += validPid
    return validBirth and validIssue and validExpiration and validHeight and validHair and validEye and validPid

def isValidYear(entry, minn, maxn):
    normalized = entry
    try:
        value = int(normalized)
        return value >= minn and value <= maxn
    except:
        return False

def isValidHeight(passport):
    h, unit = passport['hgt'][:-2], passport['hgt'][-2:]
    try:
        h = int(h)
        if unit == 'cm':
            return 150 <= h <= 193
        elif unit == 'in':
            return 59 <= h <= 76
        else:
            return False
    except:
        return False

def isValidHair(passport):
    hcl = passport['hcl']
    first, rest = hcl[0], hcl[1:]
    return first == '#' and len(rest) == 6 and all(c in '0123456789abcdef' for c in rest)

total = 0
for passport in ids:
    if is_valid(passport):
        total += 1
print(total)
print(totals)
