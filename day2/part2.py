file = open('input.txt','r')

horizontal = 0
vertical = 0
aim = 0

while True:
    line = file.readline()
    if not line:
        break

    command = line.split(' ')
    direction = command[0]
    distance = int(command[1])

    if (direction == 'forward'):
        horizontal += distance
        vertical += (aim * distance)
        print('Moving forward: %s -> (%s:%s:%s)' % (distance,horizontal,vertical,aim))
    elif (direction == 'up'):
        aim -= distance
        print('Aiming up %s -> (%s:%s:%s)' % (distance,horizontal,vertical,aim))
    elif (direction == 'down'):
        aim += distance
        print('Aiming down %s -> (%s:%s:%s)' % (distance,horizontal,vertical,aim))
    else:
        print('Invalid command: ', direction)

print("Final position is: %s:%s = %s" % (horizontal,vertical,(horizontal * vertical)))