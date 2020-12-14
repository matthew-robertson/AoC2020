from collections import defaultdict

def apply_mask(mask, value, i=0):
    if i == len(value):
        return [int(''.join(value), 2)]
    if mask[i] == '1':
        value[i] = '1'
        return apply_mask(mask, value, i+1)
    elif mask[i] == '0':
        return apply_mask(mask, value, i+1)
    else:
        v1 = value.copy()
        v1[i] = '1'
        v2 = value.copy()
        v2[i] = '0'
        return apply_mask(mask, v1, i+1) + apply_mask(mask, v2, i+1)

active_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
mem = defaultdict(int)
with open('input.txt', 'r') as ins:
    for line in ins:
        address, value = line.strip().split(' = ')
        if address[1] == 'a':
            active_mask = value
        else:
            a = int(address.split('[')[1][:-1])
            al = list(format(a, '036b'))
            a_set = apply_mask(active_mask, al)
            for new_a in a_set:
                mem[new_a] = int(value)

total = 0
for key in mem.keys():
    total += mem[key]
print('The final total in memory is: %s' % total)
