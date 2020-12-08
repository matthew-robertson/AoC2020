class opcode:
    def __init__(self, op, value):
        self.op = op
        self.amount = value
        self.seen = False

    def to_string(self):
        return({'opcode': self.op, 'amount': self.amount, 'seen': self.seen})

program = []
with open('input.txt', 'r') as ins:
    for line in ins:
        code, amount = line.split(' ')
        op = opcode(code, int(amount))
        program.append(op)

def test_path(pg):
    acc = 0
    current_command = 0
    while True:
        if current_command == len(pg):
            return True, acc

        to_execute = pg[current_command]
        if to_execute.seen:
            return False, acc

        to_execute.seen = True
        if to_execute.op == "nop":
            current_command += 1
        elif to_execute.op == 'acc':
            acc += to_execute.amount
            current_command += 1
        elif to_execute.op == "jmp":
            current_command += to_execute.amount

def reset(pg):
    for op in pg:
        op.seen = False

for (index, op) in enumerate(program):
    reset(program)
    new_program = program.copy()
    if op.op == 'jmp':
        new_program[index] = opcode('nop', op.amount)
    elif op.op == 'nop':
        new_program[index] = opcode('jmp', op.amount)
    else:
        continue

    ret, acc = test_path(new_program)
    if ret:
        print('Changed %s, giving proper execution, terminating in %s' % (index, acc))
        break
