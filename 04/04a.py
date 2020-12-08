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
            parsed_line[vals[0]] = vals[1]

def is_valid(passport):
    to_check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return passport.keys() >= to_check

total = 0
for passport in ids:
    if is_valid(passport):
        total += 1
print(total)
