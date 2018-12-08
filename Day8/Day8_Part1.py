import re

metadata_sum = 0
def parseNode(node, idx):
    global metadata_sum
    received_idx = idx
    num_childs = node[idx]
    num_metas = node[idx + 1]
    for i in range(num_childs):
        idx_shift = parseNode(node, idx + 2)
        idx += idx_shift
    for i in range(num_metas):
        metadata_sum += node[idx+i+2]
    idx += num_metas
    return idx - received_idx + 2

try:
    file = open("Input_Day8" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

line = file.readline()
tree = list(map(int, re.findall('\d+', line)))

parseNode(tree, 0)

print(metadata_sum)
