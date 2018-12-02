import re

def getWordCounts(word):
    occurrences = [0] * 26
    for char in word:
        occurrences[ord(char) - ord('a')] += 1
    return occurrences

try:
    file = open("Input_Day2" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

input_lines = file.readlines()
numOccurrence2 = 0
numOccurrence3 = 0

for line in input_lines:
    hasOccurrence2 = False
    hasOccurrence3 = False
    line = line.rstrip()
    wordCounts = getWordCounts(line)
    for count in wordCounts:
        if count == 2:
            hasOccurrence2 = True
        elif count == 3:
            hasOccurrence3 = True
    if hasOccurrence2:
        numOccurrence2 += 1
    if hasOccurrence3:
        numOccurrence3 += 1

print(numOccurrence2 * numOccurrence3)
