nums = []
with open('input.txt', 'r') as ins:
    for line in ins:
        nums.append(int(line))

answer = None
for (index, number) in enumerate(nums[25:]):
    isSum = False
    preamble = nums[index:index+25]
    for component in preamble:
        if (number - component) in preamble:
            isSum = True
            break
    if not isSum:
        print("%s, index %s is not the sum of two of the previous 25 numbers" % (number, index))
        break
    print(index)
