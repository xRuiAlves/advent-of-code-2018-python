serial_number = 4842

m = []
for i in range(300):
    m.append([0] * 300)

for i in range(300):
    for j in range(300):
        rack_id = j + 1 + 10
        power_level = (i + 1) * rack_id
        s = power_level + serial_number
        t = s * rack_id
        h = (t//100)%10
        m[i][j] = h - 5



sum = 0
x = 0
y = 0
maxsize = None

for i in range(298):
    for j in range(298):
        val = 0
        for k in range(3):
            for w in range(3):
                val += m[i+k][j+w]
        if (val > sum):
            x = j
            y = i
            sum = val

print("X: " + str(x+1))
print("Y: " + str(y+1))