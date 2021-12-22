file = open('input.txt','r')
count = 0
prevSum = -1
while True:
    line1 = file.readline()
    pos = file.tell()
    line2 = file.readline()
    line3 = file.readline()
    file.seek(pos)
    if not line3:    
        break
    sum = int(line1) + int(line2) + int(line3)
    if ((prevSum > 0) and (sum > prevSum)):
        count += 1
    prevSum = sum

print("Number of increases: ",count)