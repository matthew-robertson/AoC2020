nums = []
with open('input.txt', 'r') as ins:
    for line in ins:
        nums.append(int(line))

targetNum = 26134589
list_to_check = nums[:478]

for (index, start) in enumerate(list_to_check):
    running_total = start
    list_of_nums = [start]
    done = False
    for to_add in list_to_check[index+1:]:
        list_of_nums.append(to_add)
        running_total += to_add

        if running_total == targetNum:
            list_of_nums.sort()
            print ("Target hit! Smallest (%s) and largest (%s) sum to %s" % (list_of_nums[0], list_of_nums[-1], list_of_nums[0] + list_of_nums[-1]))
            done = True
            break
    if done:
        break
