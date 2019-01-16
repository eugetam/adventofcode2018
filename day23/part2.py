import re
with open(r'2018/day23/input.txt', 'r') as f:
    lines = f.readlines()
#pos=<135229323,40378125,32102269>, r=93910693
bots = []

for idx, line in enumerate(lines):
    x, y, z, r = re.match('pos=<(-?\d+),(-?\d+),(-?\d+)>,\s*r=(\d+)', line).groups()
    bots.append((int(x), int(y), int(z), int(r)))

minx = min(bots, key=lambda b: b[0])[0]
maxx = max(bots, key=lambda b: b[0])[0]
miny = min(bots, key=lambda b: b[1])[1]
maxy = max(bots, key=lambda b: b[1])[1]
minz = min(bots, key=lambda b: b[2])[2]
maxz = max(bots, key=lambda b: b[2])[2]

def distance(minpoint, dimsize, bot):
    d = 0
    for i in range(3):
        if bot[i] < minpoint[i] or bot[i] > (minpoint[i] + (dimsize-1)):
            d += min(abs(bot[i] - minpoint[i]), abs(bot[i] - minpoint[i] - dimsize + 1))
    return d
    
    #return abs(x-bot[0]) + abs(y-bot[1]) + abs(z-bot[2])

def num_bots_in_range(minpoint, dimsize):
    num_bots = 0
    if dimsize < 1:
        pass
    for b in bots:
        d = distance(minpoint, dimsize, b)
        if d <= b[3]:
            num_bots += 1
    return num_bots

def split_space(minpoints, dimsize):
    space_list = []
    for minpoint in minpoints:
        p1 = (minpoint[0], minpoint[1], minpoint[2])
        p2 = (minpoint[0], minpoint[1]+dimsize//2, minpoint[2])
        p3 = (minpoint[0], minpoint[1], minpoint[2]+dimsize//2)
        p4 = (minpoint[0], minpoint[1]+dimsize//2, minpoint[2]+dimsize//2)
        p5 = (minpoint[0]+dimsize//2, minpoint[1], minpoint[2])
        p6 = (minpoint[0]+dimsize//2, minpoint[1]+dimsize//2, minpoint[2])
        p7 = (minpoint[0]+dimsize//2, minpoint[1], minpoint[2]+dimsize//2)
        p8 = (minpoint[0]+dimsize//2, minpoint[1]+dimsize//2, minpoint[2]+dimsize//2)
        space_list.extend([p1, p2, p3, p4, p5, p6, p7, p8])
    return space_list

def trim(points, dimsize):
    best = ''
    origin = (0,0,0,0)
    dorigin = 100000000000
    for p in points:
        d = distance(p, dimsize, origin)
        if d < dorigin:
            best = p
            dorigin = d
    return [best]

dimsize = 1
while dimsize < (maxx-minx+1) or dimsize < (maxy-miny+1) or dimsize < (maxz-minz+1):
    dimsize *= 2
minpoints = [(minx, miny, minz)]

while True:
    subspaces = split_space(minpoints, dimsize)
    nbots = []
    for ss in subspaces:
        nbots.append(num_bots_in_range(ss, dimsize/2))
    minpoints = [(int(s[0]), int(s[1]), int(s[2])) for s, n in zip(subspaces, nbots) if n==max(nbots)]
    minpoints = set(minpoints)
    if len(minpoints) > 4:
        minpoints = trim(minpoints, dimsize)
    print(minpoints)
    if dimsize ==1:
        break
    dimsize /= 2
    print(dimsize, len(minpoints), max(nbots))

print(max(nbots))

for p in minpoints:
    print('Answer', p[0]+p[1]+p[2])