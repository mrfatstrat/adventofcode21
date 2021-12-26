file = open('input.txt','r')

xPos = 0
yPos = 0

while True:
    line = file.readline()
    if not line:
        break

    command = line.split(' ')
    direction = command[0]
    distance = int(command[1])

    if (direction == 'forward'):
        xPos += distance
        print('Moving forward: %s -> (%s:%s)' % (distance,xPos,yPos))
    elif (direction == 'up'):
        yPos -= distance
        print('Moving up: %s -> (%s:%s)' % (distance,xPos,yPos))
    elif (direction == 'down'):
        yPos += distance
        print('Moving down: %s -> (%s:%s)' % (distance,xPos,yPos))
    else:
        print('Invalid command: ', direction)

print("Final position is: %s:%s = %s" % (xPos,yPos,(xPos*yPos)))