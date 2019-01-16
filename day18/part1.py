from copy import deepcopy
with open(r'2018\day18\input.txt', 'r') as f:
    lines = f.readlines()
land = []
for line in lines:
    land.append([c for c in line.strip()])
adjs = [(-1,0), (-1,1), (-1,-1), (0,1), (0,-1), (1,0), (1,-1), (1,1)]

def draw(land):
    for y in land:
        print(''.join(y))
    print('---done----')

def tally(land):
    t = 0
    l = 0
    for r in land:
        for x in r:
            if x =='|':
                t +=1
            elif x =='#':
                l +=1
    return (t, l, t*l)    

# draw(land)
w = len(land[0])
h = len(land)
listtowrite = []
for i in range(0, 10000):
    new_land = deepcopy(land)
    for y in range(len(land)):
        row = []
        for x in range(len(land[0])):
            t, l, o = 0, 0, 0
            for a in adjs:
                if x + a[0] < 0 or x+a[0] >= w or y+a[1] < 0 or y+a[1] >= h:
                    continue
                if land[y+a[1]][x+a[0]] == '|':
                    t +=1
                if land[y+a[1]][x+a[0]] == '.':
                    o +=1
                if land[y+a[1]][x+a[0]] == '#':
                    l +=1
            if land[y][x] == '|':
                if l >= 3:
                    new_land[y][x] = '#'
            elif land[y][x] == '.':
                if t >= 3:
                    new_land[y][x] = '|'
            elif land[y][x] == '#':
                if l < 1 or t < 1:
                    new_land[y][x] = '.'
    land = new_land
    if i == 9:
        tal = tally(land)
        print('after 10 minutes ', i, tal)
    if i > 2000 and i < 2500:
        tal = tally(land)
       # print(i, tal)
        listtowrite.append(f'{i},{tal[0]},{tal[1]},{tal[2]}')
        # draw(land)
    if i == 2500:
        break

with open(r'2018/day18/output.txt', 'w') as f:
    f.write('\n'.join(listtowrite))
# for part 2, determined from this output file the periodic values and extrapolated to 1000000000 minutes