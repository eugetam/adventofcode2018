import re

with open(r'2018/day25/input.txt', 'r') as f:
    lines = f.readlines()
points = []
for line in lines:
    result = re.match(r'\s*(-?\d+),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)', line)
    if result:
        x, y, z, a = result.groups()
        points.append((int(x), int(y), int(z), int(a)))
# print(points)

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + abs(p1[3] - p2[3])

cons = []
donelist = []
while len(donelist) != len(points):
    newcon = []
    foundnew = True
    while foundnew:
        foundnew = False
        for p in points:
            if p in donelist:
                continue
            if not newcon:
                newcon.append(p)
                donelist.append(p)
                foundnew = True
                continue
            for p2 in newcon:
                if distance(p, p2) <= 3:
                    newcon.append(p)
                    donelist.append(p)
                    foundnew=True
                    break
    cons.append(newcon)

print(len(cons))
        