import sys
from enum import Enum

class LineDirection(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    OTHER = 2

class Line:
    def __init__(self, start, stop):
        if (start[0] > stop[0]) or (start[1] > stop[1]):
            # chnage direction
            self.start = stop
            self.stop = start
        else:   
            self.start = start
            self.stop = stop
        if start[0] == stop[0]:
            self.direction = LineDirection.HORIZONTAL 
        elif start[1] == stop[1]:
            self.direction = LineDirection.VERTICAL
        else:
            self.direction = LineDirection.OTHER

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
        else:
            print("Can't play with non horizontal or vertical lines, ignoring")

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

    #find max horizontal and vertical
    hvLines =  list(filter(lambda x: x.direction == LineDirection.HORIZONTAL or x.direction == LineDirection.VERTICAL ,lines))
    print("Found %s horizontal or vertical lines" % len(hvLines))
    hMax = max(map(lambda x: x.stop[0], hvLines)) + 1
    vMax = max(map(lambda x: x.stop[1], hvLines)) + 1
    field = Field(hMax,vMax)
    for hl in hvLines:
        field.addLine(hl)
    overlaps = field.countOverLaps(2)
    print("Overlaps with 2 lines or more: %s" % overlaps)

if __name__ == "__main__":
    main(sys.argv)