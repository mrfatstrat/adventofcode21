import re

file = open('input.txt','r')

lineCount = 0
zeroCount = [0] * 12
binaryPattern = re.compile("^[0,1]+$")

while True:
    line = file.readline()
    lineCount += 1
    if not line:
        break
    if not binaryPattern.match(line):
        print("Invalid line: %s" % line)
    else:
        charList = list(line)
        for i in range(len(charList)):
            if charList[i] == '0':
                    zeroCount[i] += 1

gamma = [0] * 12
epsilon = [1] * 12
for i in range(len(zeroCount)):
    if zeroCount[i] < lineCount/2:
        gamma[i] = 1
        epsilon[i] = 0

gammaDec =  int(''.join(map(str,gamma)),2)
epsilonDec =  int(''.join(map(str,epsilon)),2)
power = gammaDec * epsilonDec
print('Number of lines found: %s' % lineCount)
print('Gamma: %s' % gammaDec)
print('Epsilon: %s' % epsilonDec)
print('Power: %s' % power)