import re
file = open('input.txt','r')

expectedLength = 12
binaryPattern = re.compile("^[0,1]+$")
diagnosticReport = []

while True:
    line = file.readline().strip()
    if not line:
        break
    if not binaryPattern.match(line):
        print("Invalid line: %s" % line)
        exit
    else:
        diagnosticReport.append(line)
        if not len(line) == expectedLength:
            print('Unexpected line length: %s' %line)
            exit

totalCount = len(diagnosticReport)

# Find the oxygen generator rating
filteredList = diagnosticReport
i = 0
while len(filteredList) > 1:
    bitMap =  map(lambda x: x[i], filteredList)
    count = bitMap.count('0')
    #filter on the most common bit or 1 if eually common
    filterBit = '0' if count > (len(filteredList)/2) else '1'
    newFilteredList =  list(filter(lambda x: x[i] == filterBit, filteredList))
    filteredList = newFilteredList
    i += 1
 
oxygen = filteredList[0]
oxygenDec = int(oxygen,2)

# Find the co2 scrubber rating
filteredList = diagnosticReport
i = 0
while len(filteredList) > 1:
    bitMap =  map(lambda x: x[i], filteredList)
    count = bitMap.count('0')
    #filter on the least common bit or 0 if eually common
    filterBit = '0' if count <= (len(filteredList)/2) else '1'
    newFilteredList =  list(filter(lambda x: x[i] == filterBit, filteredList))
    filteredList = newFilteredList
    i += 1
 
co2 = filteredList[0]
co2Dec = int(co2,2)

print("Oxygen generator rating: %s -> %s" % (oxygen,oxygenDec))
print("CO2 scrubber rating: %s -> %s" % (co2,co2Dec))
print("Life support rating: %s" % (oxygenDec*co2Dec))
