import re
import matplotlib.pyplot as plt
import numpy as np

try:
    file = open("Input_Day10" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading input ***")
    raise SystemExit

lines = file.readlines()
points = []
x = []
y = []
sx = []
sy = []

for line in lines:
    [px, py, psx, psy] = map(int, re.findall('-?\d+', line))
    x.append(px)
    y.append(py)
    sx.append(psx)
    sy.append(psy)

x = np.asarray(x)
y = np.asarray(y)
sx = np.asarray(sx)
sy = np.asarray(sy)

t = 10240
x += sx * t
y += sy * t

for i in range(1000):
    print(i)
    t += 1
    x = sx * t
    y = sy * t
    plt.scatter(x, y)
    plt.show()