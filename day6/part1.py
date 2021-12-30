import sys


class Fish:
    def __init__(self, timer):
        self.timer = timer
    
    def __repr__(self):
        return "{Fish t: %s}" % self.timer

    def age(self):
        if self.timer == 0:
            # reset and spawn new fish
            self.timer = 6
            return Fish(8)
        else:
            # count down timer
            self.timer -= 1
            return None

def loadInput(filename):
    file = open(filename,'r')
    inputData = file.readlines()
    fishes = map(lambda t: Fish(int(t)), inputData[0].split(','))
    print("Found %s fishes in input file" % len(fishes))
    return fishes

def main(argv):
    if not len(argv) == 3:
        print('Invalid number of input arguments')
        exit(1)

    duration = int(argv[2])
    fishes = loadInput(argv[1])

    print("Starting reproduction simulation for %s days" % duration)    

    for d in range(1,duration+1):
        babies = []
        babies = map(lambda f: f.age(), fishes)
        babies = filter(lambda b: b != None,  babies)
        fishes += babies
        print("Day %s -> %s new born which gives %s total fishes" % (d,len(babies),len(fishes)))
    
    print('')
    print("Total number nof fished after %s days is %s" % (duration, len(fishes)))

if __name__ == "__main__":
    main(sys.argv)
    