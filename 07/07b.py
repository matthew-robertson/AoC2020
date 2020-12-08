bag_dict = {}
with open('input.txt', 'r') as ins:
    for line in ins:
        parsed_contents = {}
        bag, contents = line.split(' contain ')
        bag = bag[:-5]
        contents = contents.strip().split(', ')
        for content in contents:
            if content == 'no other bags.':
                break
            count = int(content.split(' ')[0])
            colour = ' '.join(content.split(' ')[1:-1])
            parsed_contents[colour] = count
        bag_dict[bag] = parsed_contents

def reducer(bags):
    total = 1
    if bags == {}:
        return total
    for bag in bags:
        total += reducer(bag_dict[bag]) * bags[bag]
        
    return total

print(reducer(bag_dict['shiny gold']) - 1)
