import re

class Place:
  def __init__(self, id, xi, yi):
    self.id = id
    self.xi = xi
    self.yi = yi
    self.outOfBounds = False
    self.numSquares = 0

try:
    file = open("Input_Day7" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

lines = file.readlines()
counts_map = {}
directions = {}
distinct_elems = set()

for line in lines:
    [origin, target] = re.findall("\s\w\s",line)
    origin = origin[1]
    target = target[1]
    distinct_elems.add(origin)
    distinct_elems.add(target)

    if target in counts_map:
        counts_map[target] += 1
    else:
        counts_map[target] = 1

    if origin in directions:
        directions[origin].append(target)
    else:
        directions[origin] = [target]
    
for elem in distinct_elems:
    if elem not in counts_map:
        counts_map[elem] = 0
    if elem not in directions:
        directions[elem] = []

num_elems = len(counts_map)
available_tasks = set()

for key, value in counts_map.items():
    if value == 0:
        available_tasks.add(key)

string = ""
while len(string) < num_elems:
    for elem in sorted(available_tasks):
        if counts_map[elem] == 0:
            available_tasks.remove(elem)
            string += elem
            for destin in directions[elem]:
                counts_map[destin] -= 1
                available_tasks.add(destin)
            break

print(string)


