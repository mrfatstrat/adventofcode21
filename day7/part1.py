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

def findOptimal(positions):
    finalPos = 0
    distribution = [0] * (max(positions) + 1)
    for p in positions:
        distribution[p] += 1
    optimal =  {'pos': 0, 'fuel': None}
    for pos in range(len(distribution)):
        fuelCalc =  map(lambda (i,x): x * abs(pos - i), enumerate(distribution))
        fuel = reduce(lambda x,y: x+y,fuelCalc)
        if not optimal['fuel'] or fuel < optimal['fuel']:
            optimal['pos'] = pos
            optimal['fuel'] = fuel
    return optimal

def calculateFuelConsumption(startPos,endPos):
    fuel = 0
    for p in startPos:
        fuel += abs(endPos - p)
    return fuel

def main(argv):
    if len(argv) < 2:
        print("Invalid input arguments")
        exit(1)

    positions = loadInput(argv[1])
    optimal = findOptimal(positions)
    finalPos = optimal['pos']
    fuel = optimal['fuel']
    print("The optimal position is %s and the total fuel required is %s" % (finalPos,fuel))

if __name__ == "__main__":
    main(sys.argv)