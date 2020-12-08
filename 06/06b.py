from collections import defaultdict

group_answers = []
with open('input.txt', 'r') as ins:
  parsed_line = defaultdict(int)
  for line in ins:
    if len(line.strip()) == 0:
        group_answers.append(parsed_line)
        parsed_line = defaultdict(int)
    else:
        parsed_line['group_members'] += 1
        for answer in line.strip():
            parsed_line[answer] += 1
group_answers.append(parsed_line)

total = 0
for group in group_answers:
    member_count = group['group_members']
    for key in group.keys():
        if key == 'group_members':
            continue

        total += member_count == group[key]
print(total)
