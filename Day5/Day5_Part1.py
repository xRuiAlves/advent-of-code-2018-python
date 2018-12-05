import re

diff = ord('a') - ord('A')

def match(a, b):
    global diff
    return (abs(ord(a) - ord(b)) == diff)

try:
    file = open("Input_Day5" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit
        

line = list(file.readline())
index = 0
while(index < len(line)-1):
    if (match(line[index], line[index+1])):
        del(line[index:index+2])
        index = max(index-1, 0)
    else:
        index += 1

print(len(line))
