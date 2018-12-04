import re

def getSleepyData(times):
    maxt = 0
    amount = 0
    for i in range(len(times)):
        if times[i] > amount:
            maxt = i
            amount = times[i]
    return [maxt,amount]

try:
    file = open("Input_Day4" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

input_lines = file.readlines()

shifts_info = []
for line in input_lines:
    line = line.rstrip()
    shifts_info.append(line)

shifts_info.sort()

shifts = {}
for shift in shifts_info:
    guard = re.findall("#\d+",shift)
    if (len(guard) != 0 and guard[0] not in shifts):
        shifts[guard[0]] = [0] * 60

i = 0
while i < len(shifts_info):
    guard = re.findall("#\d+",shifts_info[i])[0]
    i += 1
    last_asleep = 0
    guard_data = shifts[guard]
    while (i < len(shifts_info) and "begins shift" not in shifts_info[i]):
        if ("wakes up" in shifts_info[i]):
            time = int(shifts_info[i][15:17])
            for j in range(last_asleep, time):
                guard_data[j] += 1
        elif ("falls asleep" in shifts_info[i]):
            last_asleep = int(shifts_info[i][15:17])
            
        i += 1
    shifts[guard] = guard_data
    
max_minute = 0
max_amount = 0
sleepy_guard = None
for guard,times in shifts.items():
    data = getSleepyData(times)
    minute = data[0]
    amount = data[1]
    if (amount > max_amount):
        max_amount = amount
        max_minute = minute
        sleepy_guard = guard 

guard_id = int(sleepy_guard[1:])
print(guard_id * max_minute)
