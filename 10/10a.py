adapters = []
with open('input.py', 'r') as ins:
    for line in ins:
        adapters.append(int(line))

adapters.sort()
print(adapters)
singles = 0
triples = 1


last = 0
for adapter in adapters:
    if (adapter - last) == 1:
        singles += 1
    elif (adapter - last) == 3:
        triples += 1
    last = adapter

print("Final anser is %s singles times %s triples, for %s" % (singles, triples, singles * triples))
