file = open('input.txt','r')
count = 0
prevLine = -1
while True:
    line = file.readline()
    if not line:    
        break
    lineNumber = int(line)
    if ((prevLine > 0) and (lineNumber > prevLine)):
        count += 1
    prevLine = lineNumber

print("Number of increases: ",count)