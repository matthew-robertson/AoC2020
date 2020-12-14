import math

class ship:
    def __init__(self):
        self.facing = [1, 0]
        self.pos = [0, 0]

    def handle_command(self, key, amount):
        if key == 'N':
            self.pos[1] += amount
        elif key == 'S':
            self.pos[1] -= amount
        elif key == 'E':
            self.pos[0] += amount
        elif key == 'W':
            self.pos[0] -= amount
        elif key == 'F':
            self.pos[0] += self.facing[0] * amount
            self.pos[1] += self.facing[1] * amount
        elif key == 'L':
            rad = math.radians(amount)
            newX = self.facing[0]*math.cos(rad) - self.facing[1]*math.sin(rad)
            newY = self.facing[0]*math.sin(rad) + self.facing[1]*math.cos(rad)
            self.facing = (newX, newY)
        elif key == 'R':
            rad = math.radians(-amount)
            newX = self.facing[0]*math.cos(rad) - self.facing[1]*math.sin(rad)
            newY = self.facing[0]*math.sin(rad) + self.facing[1]*math.cos(rad)
            self.facing = [newX, newY]
        

with open('input.txt', 'r') as ins:
    s = ship()
    for line in ins:
        s.handle_command(line[0], int(line[1:]))

    print('Final position is (%s, %s), giving a solution of %s' % (s.pos[0], s.pos[1], abs(s.pos[0])+abs(s.pos[1])))
    

