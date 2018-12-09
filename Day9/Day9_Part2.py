import re

class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
        self.last = None

try:
    file = open("Input_Day9" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

input = file.readline()
[num_players, num_marbles] = map(int, re.findall('\\d+', input))
num_marbles *= 100

players = [0] * num_players
n0 = Node(0)
n1 = Node(1)
n0.next = n1
n0.last = n1
n1.next = n0
n1.last = n0
current_node = n1

for marble in range(2, num_marbles + 1):
    if marble % 23 == 0:
        for i in range(7):
            current_node = current_node.last
        players[marble % num_players] += marble + current_node.data
        current_node.last.next = current_node.next
        current_node = current_node.next
    else:
        newNode = Node(marble)
        newNode.last = current_node.next
        newNode.next = current_node.next.next
        current_node.next.next.last = newNode
        current_node.next.next = newNode
        current_node = newNode

print(max(players))