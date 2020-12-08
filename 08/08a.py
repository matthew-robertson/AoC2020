class opcode:
    def __init__(self, op, value):
        self.op = op
        self.amount = value
        self.seen = False

program = []
with open('input.txt', 'r') as ins:
    for line in ins:
        code, amount = line.split(' ')
        op = opcode(code, int(amount))
        program.append(op)

acc = 0
current_command = 0
while True:
    to_execute = program[current_command]

    if to_execute.seen:
        print("Final acc: %s" % acc)
        break

    to_execute.seen = True
    if to_execute.op == "nop":
        current_command += 1
    elif to_execute.op == 'acc':
        acc += to_execute.amount
        current_command += 1
    elif to_execute.op == "jmp":
        current_command += to_execute.amount

