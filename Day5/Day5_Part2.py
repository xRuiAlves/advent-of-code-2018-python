import re

diff = ord('a') - ord('A')

def match(a, b):
    global diff
    return (abs(ord(a) - ord(b)) == diff)

def createPolyWithoutAthom(string, athom):
    global diff
    poly = []
    for char in string:
        if (char != athom and ord(char) != ord(athom) + diff):
            poly.append(char)
    return poly

def getPolySize(line):
    index = 0
    while(index < len(line)-1):
        if (match(line[index], line[index+1])):
            del(line[index:index+2])
            index = max(index-1, 0)
        else:
            index += 1
    return len(line)

try:
    file = open("Input_Day5" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit
    
line = file.readline()

polymers = []
for c in range(ord('B'), ord('B')+25):
    polymers.append(chr(c))

lineWithoutPoly = createPolyWithoutAthom(line, 'A')
minimum = getPolySize(lineWithoutPoly)

for poly in polymers:
    lineWithoutPoly = createPolyWithoutAthom(line, poly)
    val = getPolySize(lineWithoutPoly)
    minimum = min(val, minimum)

print(minimum)


