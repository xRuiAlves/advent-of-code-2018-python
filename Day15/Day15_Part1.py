import re

class Unit: 
    def __init__(self, type): 
        self.type = type
        self.updated = False
        if type == 'E' or type == 'G':
            self.hp = 200
        else:
            self.hp = -1

def empty_cell(cell):
    return cell.type == '.'

def other_type(type):
    if type == 'E':
        return 'G'
    if type == 'G':
        return 'E'
    return None

def get_enemy(i, j):
    global m
    my_type = m[i][j].type
    enemies = []
    if m[i-1][j].type == other_type(my_type):
        enemies.append([i-1, j])
    if m[i][j-1].type == other_type(my_type):
        enemies.append([i, j-1])
    if m[i][j+1].type == other_type(my_type):
        enemies.append([i, j+1])
    if m[i+1][j].type == other_type(my_type):
        enemies.append([i+1, j])

    enemy = None
    if (len(enemies) > 0):
        enemy = enemies[0]
        min_hp = m[enemy[0]][enemy[1]].hp
        for k in range(1, len(enemies)):
            [ei, ej] = enemies[k]
            if m[ei][ej].hp < min_hp:
                min_hp = m[ei][ej].hp
                enemy = [ei, ej]

    return enemy

def get_nearest_enemy(i, j):
    global m
    my_type = m[i][j].type
    squares = []
    visited = []
    to_visit = [[i, j]]
    while len(to_visit) > 0:
        new_to_visit = []
        for [i, j] in to_visit:
            if [i, j] in visited:
                continue
            else:
                visited.append([i,j])
            if square_near_enemy(i, j, my_type):
                squares.append([i,j])
            else:
                for [a,b] in [[i-1, j], [i,j-1], [i,j+1], [i+1,j]]:
                    if (empty_cell(m[a][b])):
                        new_to_visit.append([a,b])
        if (len(squares) > 0):
            return sorted(squares)[0]
        to_visit = new_to_visit
    return None

def get_shortest_path(origin_i, origin_j, target_i, target_j):
    global m
    connections = [[None, None, origin_i, origin_j]]   
    visited = []
    to_visit = [[origin_i, origin_j]]
    found = False
    while len(to_visit) > 0 and not found:
        [i, j] = to_visit[0]    
        del to_visit[0]
        
        for [a,b] in [[i-1, j], [i,j-1], [i,j+1], [i+1,j]]:
            if empty_cell(m[a][b]) and [a,b] not in visited:
                to_visit.append([a,b])
                visited.append([a,b])
                connections.append([i, j, a, b])
                if [a,b] == [target_i, target_j]:
                    found = True
                    break

    idx = len(connections) - 1
    path = [connections[idx][2:4], connections[idx][0:2]]
    while idx != 0:
        next = connections[idx][0:2]
        for i in range(len(connections)):
            if connections[i][2:4] == next:
                path.append(connections[i][0:2])
                idx = i
                break
    return list(reversed(path))[1:]

def square_near_enemy(i, j, my_type):
    o_type = other_type(my_type)
    return m[i+1][j].type == o_type or m[i-1][j].type == o_type or m[i][j+1].type == o_type or m[i][j-1].type == o_type


def attack(i, j):
    global m, num_elfs, num_goblins
    m[i][j].hp -= 3
    if m[i][j].hp <= 0:
        if m[i][j].type == 'G':
            num_goblins -= 1
        elif m[i][j].type == 'E':
            num_elfs -= 1
        m[i][j] = Unit('.')

try:
    file = open("Input_Day15" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

lines = file.readlines()
m = []
num_goblins = num_elfs = 0

for line in lines:
    line = list(line.rstrip())
    mline = []
    for cell in line:
        mline.append(Unit(cell))
        if cell == 'G':
            num_goblins += 1
        elif cell == 'E':
            num_elfs += 1
    m.append(mline)

round = -1
while num_goblins > 0 and num_elfs > 0:
    round += 1
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j].updated = False

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j].type == 'G' or m[i][j].type == 'E':
                if m[i][j].updated:
                    continue
                m[i][j].updated = True
                enemy = get_enemy(i,j)
                if enemy != None:
                    attack(enemy[0], enemy[1])
                else:
                    enemy = get_nearest_enemy(i,j)
                    if enemy == None:
                        continue
                    [ni, nj] = get_shortest_path(i, j, enemy[0], enemy[1])[1]
                    m[ni][nj] = m[i][j]
                    m[i][j] = Unit('.')
                    enemy = get_enemy(ni,nj)
                    if enemy != None:
                        attack(enemy[0], enemy[1])

winner_type = None
if num_elfs > 0:
    winner_type = 'E'
else:
    winner_type = 'G'

hp_sum = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j].type == winner_type:
            hp_sum += m[i][j].hp


print('Elves: ' + str(num_elfs))
print('Goblins: ' + str(num_goblins))
print('Round: ' + str(round))
print('HP sum: ' + str(hp_sum))
print('Output: ' + str(round * hp_sum))