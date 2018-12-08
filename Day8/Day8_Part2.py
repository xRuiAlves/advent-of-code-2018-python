import re

def parseNode(node, idx):
    received_idx = idx
    num_childs = node[idx]
    num_metas = node[idx + 1]
    child_values = [0] * num_childs
    my_metas = [0] * num_metas

    for i in range(num_childs):
        [idx_shift, child_values[i]] = parseNode(node, idx + 2)
        idx += idx_shift

    my_meta = 0
    for i in range(num_metas):
        my_meta += node[idx+i+2]
        my_metas[i] = node[idx+i+2]
    idx += num_metas

    if (num_childs == 0):
        return [idx - received_idx + 2, my_meta]
    else:
        my_val = 0
        for index in my_metas:
            if index < len(child_values) + 1:
                my_val += child_values[index-1]
        return [idx - received_idx + 2, my_val]

try:
    file = open("Input_Day8" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

line = file.readline()
tree = list(map(int, re.findall('\d+', line)))

[idx, value] = parseNode(tree, 0)

print(value)
