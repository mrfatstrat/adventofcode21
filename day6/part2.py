import sys


def loadInput(filename):
    file = open(filename,'r')
    inputData = file.readlines()
    fishes = map(lambda t: int(t), inputData[0].split(','))
    fishCounter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for f in fishes:
        fishCounter[f] += 1
    print("Found %s fishes in input file" % len(fishes))
    return fishCounter

def main(argv):
    if not len(argv) == 3:
        print('Invalid number of input arguments')
        exit(1)

    duration = int(argv[2])
    fishCounter = loadInput(argv[1])
    print("Initial distribution is:")
    print(fishCounter)

    print("Starting reproduction simulation for %s days" % duration)    
    for d in range(1,duration+1):
        newFishCounter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
        for k in fishCounter.keys():
            if k == 0:
                newFishCounter[8] = fishCounter[k]
                newFishCounter[6] += fishCounter[0]      
            else:
                newFishCounter[k-1] += fishCounter[k]
        fishCounter = newFishCounter

    total = sum(fishCounter.values())
    print("Final distribution is:")
    print(fishCounter)
    print("Total number of fish after %s days is %s" % (duration, total))

if __name__ == "__main__":
    main(sys.argv)
    