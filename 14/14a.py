from collections import defaultdict

def apply_mask(mask, value):
    val_str = list(format(value, '036b'))
    for (i, c) in enumerate(mask):
        if c == '0':
            val_str[i] = '0'
        elif c == '1':
            val_str[i] = '1'
    return int(''.join(val_str), 2)

active_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
mem = defaultdict(int)
with open('input.txt', 'r') as ins:
    for line in ins:
        address, value = line.strip().split(' = ')
        if address[1] == 'a':
            active_mask = value
        else:
            a = address.split('[')[1][:-1]
            mem[a] = apply_mask(active_mask, int(value))

total = 0
for key in mem.keys():
    total += mem[key]
print('The final total in memory is: %s' % total)
