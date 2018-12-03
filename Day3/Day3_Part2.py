import re

matrix = []
matrix_size = 1000
for i in range(matrix_size):
    matrix.append([0] * matrix_size)

def verifyClaim(id, x, y, width, height):
    global matrix
    for i in range(y, y+height):
        for j in range(x, x+width):
            if matrix[j][i] != id:
                return False
    return True


def performClaim(id, x, y, width, height):
    global matrix
    for i in range(y, y+height):
        for j in range(x, x+width):
            if matrix[j][i] == 0:
                matrix[j][i] = id
            else:
                matrix[j][i] = -1
    return 

try:
    file = open("Input_Day3" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

input_lines = file.readlines()
claims = []

for line in input_lines:
    numbers = re.findall("\d+",line)
    claims.append([int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3]), int(numbers[4])])
    performClaim(int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3]), int(numbers[4]))

for claim in claims:
    if (verifyClaim(claim[0], claim[1], claim[2], claim[3], claim[4])):
        print(claim[0])
        break





