import re

def turn_left(direction):
    if direction == '<':
        return 'v'
    elif direction == 'v':
        return '>'
    elif direction == '>':
        return '^'
    elif direction == '^':
        return '<'

def turn_right(direction):
    if direction == '<':
        return '^'
    elif direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'


try:
    file = open("Input_Day13" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

lines =file.readlines()

m = []
for line in lines:
    m.append(list(line.rstrip()))

cars = []
car_symbols = ['<','>','^','v']
idt = 1
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] in car_symbols:
            cars.append([j, i, m[i][j], 0, idt])
            idt += 1

while len(cars) > 1:
    new_cars = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            for c in cars:
                if c[1] == i and c[0] == j:
                    new_cars.append(c)

    cars = new_cars
    to_remove = []
    for c in cars:
        if c[4] in to_remove:
            continue
        if c[2] == '>':
            c[0] += 1
        elif c[2] == '<':
            c[0] -= 1
        elif c[2] == '^':
            c[1] -= 1
        elif c[2] == 'v':
            c[1] += 1
        for i in range(len(cars)):
            for j in range(len(cars)):
                if i < j:
                    if cars[i][0] == cars[j][0] and cars[i][1] == cars[j][1]:
                        to_remove.append(cars[i][4])
                        to_remove.append(cars[j][4])
                        break

    new_cars = []
    for c in cars:
        if (c[4] not in to_remove):
            new_cars.append(c)
        else:
            print('Removing car ' + str(c[4]))
    cars = new_cars

    for c in cars:
        if m[c[1]][c[0]] == '\\' and c[2] == '>':
            c[2] = 'v'
        elif m[c[1]][c[0]] == '/' and c[2] == '>':
            c[2] = '^'
        elif m[c[1]][c[0]] == '\\' and c[2] == '<':
            c[2] = '^'
        elif m[c[1]][c[0]] == '/' and c[2] == '<':
            c[2] = 'v'
        elif m[c[1]][c[0]] == '\\' and c[2] == '^':
            c[2] = '<'
        elif m[c[1]][c[0]] == '/' and c[2] == '^':
            c[2] = '>'
        elif m[c[1]][c[0]] == '\\' and c[2] == 'v':
            c[2] = '>'
        elif m[c[1]][c[0]] == '/' and c[2] == 'v':
            c[2] = '<'
        elif m[c[1]][c[0]] == '+' and c[3]%3 == 0:
            c[3] += 1
            c[2] = turn_left(c[2])
        elif m[c[1]][c[0]] == '+' and c[3]%3 == 1:
            c[3] += 1
        elif m[c[1]][c[0]] == '+' and c[3]%3 == 2:
            c[3] += 1
            c[2] = turn_right(c[2])
    
print(cars)