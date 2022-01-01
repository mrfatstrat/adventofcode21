import sys

def loadInput(fileName):
    print("Loading input from: %s" % fileName)
    file = open(fileName)
    lines = file.readlines()
    positions = []
    for l in lines:
        positions += map(int, l.split(','))
    print("Found %s crabs with positions" % len(positions))
    return positions

def cFuel(start,stop):
    distance = abs(stop-start) + 1
    fuel = distance * (distance - 1) / 2
    return fuel

def findOptimal(positions):
    finalPos = 0
    distribution = [0] * (max(positions) + 1)
    for p in positions:
        distribution[p] += 1
    optimal =  {'pos': 0, 'fuel': None}
    for pos in range(len(distribution)):
        fuel = reduce(lambda x,y: x+y, map(lambda (i,x): x * cFuel(pos,i), enumerate(distribution)))
        if not optimal['fuel'] or fuel < optimal['fuel']:
            optimal= {'pos': pos, 'fuel': fuel}
    return optimal

def main(argv):
    if len(argv) < 2:
        print("Invalid input arguments")
        exit(1)

    positions = loadInput(argv[1])
    optimal = findOptimal(positions)
    pos = optimal['pos']
    fuel = optimal['fuel']
    print("The optimal position is %s and the total fuel required is %s" % (pos,fuel))

if __name__ == "__main__":
    main(sys.argv)