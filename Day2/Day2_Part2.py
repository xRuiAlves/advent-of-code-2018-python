import re

def getCountDifference(word1, word2):
    diff = 0
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            diff += 1
    return diff

def getUniqueString(word1, word2):
    uniqueString = ""
    for i in range(0, len(word1)):
        if word1[i] == word2[i]:
            uniqueString += word1[i]
    return uniqueString

try:
    file = open("Input_Day2" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

input_lines = file.readlines()
parsed_input_lines = []

for line in input_lines:
    line = line.rstrip()
    parsed_input_lines.append(line)

for i in range(0, len(parsed_input_lines)):
    for j in range(0, len(parsed_input_lines)):
        if i != j:
            diff = getCountDifference(parsed_input_lines[i], parsed_input_lines[j])
            if diff == 1:
                print(getUniqueString(parsed_input_lines[i], parsed_input_lines[j]))
                exit()
