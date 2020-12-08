group_answers = []
with open('input.txt', 'r') as ins:
  parsed_line = {}
  for line in ins:
    if len(line.strip()) == 0:
        group_answers.append(parsed_line)
        parsed_line = {}
    else:
        for answer in line.strip():
            parsed_line[answer] = True
group_answers.append(parsed_line)

group_totals = [len(answers.keys()) for answers in group_answers]
print(group_totals)
print(sum(group_totals))
