buses = []
full_data = open("input.txt", 'r')
full_text = full_data.read()
earliest, schedule = full_text.strip().split('\n')
schedule = schedule.split(',')

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

moduli = []
ids = []
i = 0
for (i, bus) in enumerate(schedule):
    if bus == 'x':
        continue
    ids.append(int(bus))
    moduli.append(int(bus)-i)

print(moduli)
print(ids)
print(chinese_remainder(ids, moduli))
full_data.close()
