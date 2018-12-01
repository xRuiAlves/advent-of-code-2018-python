import re

try:
    file = open("Input_Day1" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

input_lines = file.readlines()

sum = 0
for line in input_lines:
    num = line.rstrip()
    sum += int(num)

print(sum)
