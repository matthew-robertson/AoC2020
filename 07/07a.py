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


potential_holders = {bag for bag in bag_dict if 'shiny gold' in bag_dict[bag].keys()}
previous_p_holders = set()
while not previous_p_holders == potential_holders:
    previous_p_holders = potential_holders.copy()
    potential_holders |= {bag for bag in bag_dict if (any(colour in bag_dict[bag].keys() for colour in potential_holders))}

print(len(potential_holders))
