import re

class Place:
  def __init__(self, id, xi, yi):
    self.id = id
    self.xi = xi
    self.yi = yi
    self.outOfBounds = False
    self.numSquares = 0

def manDistance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def isSuperClose(matrix, places, i, j, boundry):
    sum = 0
    for p in places:
        d = manDistance(p.xi, j, p.yi, i)
        sum += d
    if sum >= boundry:
        return 0
    else:
        return 1

try:
    file = open("Input_Day6" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit
        

lines = file.readlines()
places = []
xmax = 0
ymax = 0

for i in range(len(lines)):
    line = lines[i].rstrip()
    [x, y] = map(int, re.findall("\d+", line))
    xmax = max(x, xmax)
    ymax = max(y, ymax)
    p = Place(i + 1, x, y)
    places.append(p)

xmax += 1
ymax += 1

matrix = []
for i in range(ymax):
    matrix.append([0] * xmax)

for p in places:
    matrix[p.yi][p.xi] = p.id

boundry = 10000

sum = 0
for i in range(ymax):
    for j in range(xmax):
        matrix[i][j] = isSuperClose(matrix, places, i, j, boundry)
        sum += matrix[i][j]

print(sum)
