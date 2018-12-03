import re

matrix = []
matrix_size = 1000
for i in range(matrix_size):
    matrix.append([0] * matrix_size)

def countOverlaps():
    overlaps = 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[j][i] > 1:
                overlaps += 1
    return overlaps

def performClaim(x, y, width, height):
    global matrix
    for i in range(y, y+height):
        for j in range(x, x+width):
            matrix[j][i] += 1
    return 

try:
    file = open("Input_Day3" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

input_lines = file.readlines()

for line in input_lines:
    numbers = re.findall("\d+",line)
    performClaim(int(numbers[1]), int(numbers[2]), int(numbers[3]), int(numbers[4]))

print(countOverlaps())

