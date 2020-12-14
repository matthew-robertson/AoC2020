import math

class ship:
    def __init__(self):
        self.waypoint = [10, 1]
        self.pos = [0, 0]

    def handle_command(self, key, amount):
        if key == 'N':
            self.waypoint[1] += amount
        elif key == 'S':
            self.waypoint[1] -= amount
        elif key == 'E':
            self.waypoint[0] += amount
        elif key == 'W':
            self.waypoint[0] -= amount
        elif key == 'F':
            self.pos[0] += self.waypoint[0] * amount
            self.pos[1] += self.waypoint[1] * amount
        elif key == 'L':
            rad = math.radians(amount)
            newX = self.waypoint[0]*math.cos(rad) - self.waypoint[1]*math.sin(rad)
            newY = self.waypoint[0]*math.sin(rad) + self.waypoint[1]*math.cos(rad)
            self.waypoint = [newX, newY]
        elif key == 'R':
            rad = math.radians(-amount)
            newX = self.waypoint[0]*math.cos(rad) - self.waypoint[1]*math.sin(rad)
            newY = self.waypoint[0]*math.sin(rad) + self.waypoint[1]*math.cos(rad)
            self.waypoint = [newX, newY]

with open('input.txt', 'r') as ins:
    s = ship()
    for line in ins:
        s.handle_command(line[0], int(line[1:]))

    print('Final position is (%s, %s), giving a solution of %s' % (s.pos[0], s.pos[1], abs(s.pos[0])+abs(s.pos[1])))
    

