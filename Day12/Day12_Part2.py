import re

try:
    file = open("Input_Day12" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

lines =file.readlines()

idx0 = 500
init_state = lines[0][15:].rstrip()
init_state = ['.']*idx0 + list(init_state) + ['.']*idx0


changes = {}

for i in range(2, len(lines)):
    pattern = lines[i][0:5]
    consequence = lines[i][9]
    changes[pattern] = consequence

state = init_state
oldsum = 0
diff = None
num_gens = 300
for generation in range(num_gens):
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
    diff = sum - oldsum
    oldsum = sum

res = int(sum + (50e9 - num_gens) * diff)
print(res)

