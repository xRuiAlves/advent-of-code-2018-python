import re

try:
    file = open("Input_Day1" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

input_lines = file.readlines()
index = 0
frequencies = {0}

sum = 0
while True:
    line = input_lines[index]
    num = line.rstrip()
    sum += int(num)
    if sum in frequencies:
        print(sum)
        break
    else:
        frequencies.add(sum)
    index = (index + 1) % len(input_lines)
