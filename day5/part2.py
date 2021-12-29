import sys
from enum import Enum

class LineDirection(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL = 2

class Line:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        if start[0] == stop[0]:
            self.direction = LineDirection.HORIZONTAL 
        elif start[1] == stop[1]:
            self.direction = LineDirection.VERTICAL
        else:
            self.direction = LineDirection.DIAGONAL
        if not self.direction == LineDirection.DIAGONAL: 
            if (start[0] > stop[0]) or (start[1] > stop[1]):
                # chnage direction
                self.start = stop
                self.stop = start

    def __repr__(self):
        return "Line (%s) %s -> %s" % (self.direction, self.start, self.stop)

class Field:
    def __init__(self, hMax, vMax):
        self.hMax = hMax
        self.vMax = vMax
        self.field = [ [0] * vMax for i in range(hMax) ]

    def __repr__(self):
        return str(self.field)

    def addLine(self,line):
        if  line.direction == LineDirection.HORIZONTAL:
            r = line.start[0]
            for c in range(line.start[1],line.stop[1]+1):
                self.field[r][c] += 1
                #print("Added +1 to: [%s,%s] now: %s" % (r,c, self.field[r][c]))
        elif line.direction == LineDirection.VERTICAL:
            c = line.start[1]
            for r in range(line.start[0],line.stop[0]+1):
                self.field[r][c] += 1
                #print("Added +1 to: [%s,%s] now: %s" % (r,c, self.field[r][c]))
        elif line.direction == LineDirection.DIAGONAL:
            hStep = -1 if line.start[0] > line.stop[0] else 1
            vStep = -1 if line.start[1] > line.stop[1] else 1
            mark = line.start
            while True:
                self.field[mark[0]][mark[1]] += 1
                if mark == line.stop:
                    break
                else:
                    mark[0] += hStep
                    mark[1] += vStep
        else:
            print("Weird line directions, ignoring")

    def countOverLaps(self, minimum):
        counter = 0
        for f in self.field:
            counter += sum(map(lambda x: x >= minimum, f))
        return counter

def parseInput(fileName):
    file  = open(fileName,'r')
    lines = file.readlines()
    return lines

def main(argv):
    input = parseInput(argv[1])
    lines = []
    for l in input:
        coordinates = map(lambda x: x.split(','), l.split('->'))
        coordinates[0] = map(int,map(lambda x: x.strip(),coordinates[0]))
        coordinates[1] = map(int,map(lambda x: x.strip(),coordinates[1]))
        lines.append(Line(coordinates[0],coordinates[1]))
    print("Found %s lines" % len(lines))
    hMax = max(map(lambda x: x.stop[0], lines)) + 1
    vMax = max(map(lambda x: x.stop[1], lines)) + 1
    field = Field(hMax,vMax)
    for hl in lines:
        field.addLine(hl)
    overlaps = field.countOverLaps(2)
    print("Overlaps with 2 lines or more: %s" % overlaps)

if __name__ == "__main__":
    main(sys.argv)