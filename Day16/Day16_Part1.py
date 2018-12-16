import re

class Test: 
    def __init__(self, before, op, after): 
        self.before = before
        self.op = op
        self.after = after

try:
    file = open("Input_Day16_Part1" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

lines = file.readlines()

idx = 0
log = []
before = operation = after = 0
for line in lines:
    if idx%4 == 0:
        before = list(map(int, re.findall('\\d+', line)))
    elif idx%4 == 1:
        operation = list(map(int, re.findall('\\d+', line)))
    elif idx%4 == 2:
        after = list(map(int, re.findall('\\d+', line)))
        log.append(Test(before, operation, after))
    idx += 1

num_samples = 0
for test in log:
    rops = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']
    if test.after[test.op[3]] != (test.before[test.op[1]] + test.op[2]):
        rops.remove('addi')
    if test.after[test.op[3]] != (test.before[test.op[1]] + test.before[test.op[2]]):
        rops.remove('addr')
    if test.after[test.op[3]] != (test.before[test.op[1]] * test.op[2]):
        rops.remove('muli')
    if test.after[test.op[3]] != (test.before[test.op[1]] * test.before[test.op[2]]):
        rops.remove('mulr')
    if test.after[test.op[3]] != (test.before[test.op[1]] & test.op[2]):
        rops.remove('bani')
    if test.after[test.op[3]] != (test.before[test.op[1]] & test.before[test.op[2]]):
        rops.remove('banr')
    if test.after[test.op[3]] != (test.before[test.op[1]] | test.op[2]):
        rops.remove('bori')
    if test.after[test.op[3]] != (test.before[test.op[1]] | test.before[test.op[2]]):
        rops.remove('borr')
    if test.after[test.op[3]] != test.op[1]:
        rops.remove('seti')
    if test.after[test.op[3]] != test.before[test.op[1]]:
        rops.remove('setr')
    if (test.op[1] > test.before[test.op[2]] and test.after[test.op[3]] != 1) or (test.op[1] <= test.before[test.op[2]] and test.after[test.op[3]] != 0):
        rops.remove('gtir')
    if (test.before[test.op[1]] > test.op[2] and test.after[test.op[3]] != 1) or (test.before[test.op[1]] <= test.op[2] and test.after[test.op[3]] != 0):
        rops.remove('gtri')
    if (test.before[test.op[1]] > test.before[test.op[2]] and test.after[test.op[3]] != 1) or (test.before[test.op[1]] <= test.before[test.op[2]] and test.after[test.op[3]] != 0):
        rops.remove('gtrr')
    if (test.op[1] == test.before[test.op[2]] and test.after[test.op[3]] != 1) or (test.op[1] != test.before[test.op[2]] and test.after[test.op[3]] != 0):
        rops.remove('eqir')
    if (test.before[test.op[1]] == test.op[2] and test.after[test.op[3]] != 1) or (test.before[test.op[1]] != test.op[2] and test.after[test.op[3]] != 0):
        rops.remove('eqri')
    if (test.before[test.op[1]] == test.before[test.op[2]] and test.after[test.op[3]] != 1) or (test.before[test.op[1]] != test.before[test.op[2]] and test.after[test.op[3]] != 0):
        rops.remove('eqrr')

    if (len(rops) >= 3):
        num_samples += 1

print(num_samples)