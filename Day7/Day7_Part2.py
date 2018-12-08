import re

class Worker:
    def __init__(self):
        self.task = None
        self.task_time = 0
    def isFree(self):
        return self.task == None
    def reset(self):
        self.task = None
        self.task_time = 0
    def assignTask(self, task, task_time):
        self.task = task
        self.task_time = task_time

def freeWorkers(workers, num_available_tasks):
    num_free_workers = 0
    for worker in workers:
        if worker.isFree():
            num_free_workers += 1
    num_ocuppied_workers = len(workers) - num_free_workers
    return num_free_workers > 0 and num_available_tasks - num_ocuppied_workers > 0

def getNumAvailableTasks(available_tasks, counts_map):
    num_available_tasks = 0
    for task in available_tasks:
        if counts_map[task] == 0:
            num_available_tasks += 1
    return num_available_tasks

def getWorkersTasks(workers):
    worker_tasks = [0] * len(workers)
    for i in range(len(workers)):
        worker_tasks[i] = workers[i].task
    return worker_tasks

try:
    file = open("Input_Day7" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

order = "GDHOSUXACIMRTPWNYJLEQFVZBK"   #Part 1 result

# Create workers
workers = []
for i in range(5):
    workers.append(Worker())

current_time = 0

lines = file.readlines()
counts_map = {}
directions = {}
task_times = {}
distinct_elems = set()

for line in lines:
    [origin, target] = re.findall(" \\w ",line)
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
    
# Add missing elements to counts map
for elem in distinct_elems:
    if elem not in counts_map:
        counts_map[elem] = 0
    if elem not in directions:
        directions[elem] = []

available_tasks = set()

# Taks times
for key, value in counts_map.items():
    task_times[key] = 61 + ord(key) - ord('A')
    if value == 0:
        available_tasks.add(key)

string = ""
while len(string) < len(distinct_elems):
    # Verify Completed Tasks
    for elem in sorted(available_tasks):
        if counts_map[elem] == 0 and task_times[elem] == 0:
            for worker in workers:
                if worker.task == elem:
                    worker.reset()
            available_tasks.remove(elem)
            string += elem
            for destin in directions[elem]:
                counts_map[destin] -= 1
                available_tasks.add(destin)   
    # Assign workers
    num_available_tasks = getNumAvailableTasks(available_tasks, counts_map)
    while(freeWorkers(workers, num_available_tasks)):
        for elem in sorted(available_tasks):
            if counts_map[elem] == 0 and elem not in getWorkersTasks(workers):
                for worker in workers:
                    if worker.isFree():
                        worker.assignTask(elem, task_times[elem])
                        break
    # Advance time
    current_time += 1
    for worker in workers:
        if not worker.isFree():
            worker.task_time -= 1
            task_times[worker.task] -= 1

print(current_time - 1)
