from collections import defaultdict
import datetime

start = datetime.datetime.now()
adapters = []
with open('input.py', 'r') as ins:
    for line in ins:
        adapters.append(int(line))

adapters.sort()

possible_combos = defaultdict(int) 
possible_combos[adapters[-1]] = 1
for adapter in adapters[-2::-1]:
    possible_combos[adapter] = 0
    possible_combos[adapter] += possible_combos[adapter+1]
    possible_combos[adapter] += possible_combos[adapter+2]
    possible_combos[adapter] += possible_combos[adapter+3]

print("The final answer is: %s" % (possible_combos[1] + possible_combos[2] + possible_combos[3]))
print((datetime.datetime.now() - start).microseconds)
