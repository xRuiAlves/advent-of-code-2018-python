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

def getClosestId(matrix, places, i, j):
    bestRepeated = False
    bestd = manDistance(places[0].xi, j, places[0].yi, i)
    bestPlace = places[0].id
    for k in range(1, len(places)):
        newd = manDistance(places[k].xi, j, places[k].yi, i)
        if newd == 0:
            return places[k].id
        elif newd == bestd:
            bestRepeated = True
        elif newd < bestd:
            bestRepeated = False
            bestd = newd
            bestPlace = places[k].id

    if (bestRepeated):
        return 0
    else:
        return bestPlace

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

for i in range(ymax):
    for j in range(xmax):
        matrix[i][j] = getClosestId(matrix, places, i, j)   
        if (i == 0 or j == 0 or i == ymax-1 or j == xmax-1):
            places[matrix[i][j] - 1].outOfBounds = True
        else:
            places[matrix[i][j] - 1].numSquares += 1 

maximum = 0
for p in places:
    if not p.outOfBounds:
        maximum = max(maximum, p.numSquares)

print(maximum)