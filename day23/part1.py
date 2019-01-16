import re
with open(r'2018/day23/input.txt', 'r') as f:
    lines = f.readlines()
#pos=<135229323,40378125,32102269>, r=93910693
bots = []
maxr = 0
for idx, line in enumerate(lines):
    result = re.match('pos=<(-*\d+),(-*\d+),(-*\d+)>,\s*r=(\d+)', line)
    bots.append([
                int(result.group(4)), int(result.group(1)), 
                int(result.group(2)), int(result.group(3))
                ])
    if int(result.group(4)) > maxr:
        bestbot = idx
        maxr = int(result.group(4))

print(bots[bestbot], maxr)

bb = bots[bestbot]
count = 0
for b in bots:
    if abs(b[1] - bb[1]) + abs(b[2] - bb[2]) + abs(b[3] - bb[3]) <= maxr:
        count += 1

print(count)