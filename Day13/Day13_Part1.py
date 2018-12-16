import re

try:
    file = open("Input_Day13" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

turn_left = {
    '<': 'v',
    'v': '>',
    '>': '^',
    '^': '<'
}

turn_right = {
    '<': '^',
    '^': '>',
    '>': 'v',
    'v': '<'
}

lines =file.readlines()

m = []
for line in lines:
    m.append(list(line.rstrip()))

cars = []
car_symbols = ['<','>','^','v']
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] in car_symbols:
            cars.append([j, i, m[i][j], 0])

while True:
    new_cars = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            for c in cars:
                if c[1] == i and c[0] == j:
                    new_cars.append(c)

    cars = new_cars
    for c in cars:
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
                        print(str(cars[i][0]) + ", " + str(cars[i][1]))
                        raise SystemExit
        
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
        elif m[c[1]][c[0]] == '+':
            c[3] += 1
            if c[3]%3 == 0:
                c[2] = turn_left[c[2]]
            elif c[3]%3 == 2:
                c[2] = turn_right[c[2]]

            
             and 
        elif m[c[1]][c[0]] == '+' and c[3]%3 == 1:
            c[3] += 1
        elif m[c[1]][c[0]] == '+' and c[3]%3 == 2:
            c[3] += 1
            c[2] = turn_right[c[2]]
    
            
                