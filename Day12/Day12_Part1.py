import re

try:
    file = open("Input_Day12" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

lines =file.readlines()

init_state = lines[0][15:].rstrip()
init_state = ['.']*50 + list(init_state) + ['.']*50

idx0 = 50

changes = {}

for i in range(2, len(lines)):
    pattern = lines[i][0:5]
    consequence = lines[i][9]
    changes[pattern] = consequence

state = init_state
for generation in range(20):
    new_state = ['.', '.']
    for i in range(2, len(state) - 2):
        pp = state[i-2]+state[i-1]+state[i]+state[i+1]+state[i+2]
        if pp in changes:
            new_state.append(changes[pp])
        else:
            new_state.append('.')
    new_state.append('.')
    new_state.append('.')
    state = new_state

sum = 0
for i in range(len(state)):
    if (state[i] == '#'):
        sum += i - idx0
print(sum)
