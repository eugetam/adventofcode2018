# cave making + rescue
import time
from copy import deepcopy

# puzzle input
depth = 11820
target = (7,782)

# test input
# depth = 510
# target = (10,10)


def draw(grid, console):
    write_list = []
    for row in grid:
        if console:
            print(','.join([str(x) for x in row]))
        write_list.append(','.join([str(x) for x in row]))
    return write_list


def erosion(loc):
    if loc[1] == 0:
        grid[loc[1]][loc[0]] = ((loc[0]*16807 + depth) % 20183) 
        return
    if loc[0] == 0:
        grid[loc[1]][loc[0]] = ((loc[1]*48271 + depth) % 20183) 
        return
    grid[loc[1]][loc[0]] = ((grid[loc[1]-1][loc[0]] * grid[loc[1]][loc[0]-1]  + depth) % 20183) 
    return


def drawm(mgrid):
    # listtowrite = []
    rowstr = []
    tools = ['t','c','n']
    listtowrite = []
    for row in mgrid:
        rowstr = []
        for d in row:
            valstr = []
            for t in tools:
                val = d.get(t, 0)
                valstr.append(f'{val:04d}')
            rowstr.append('|'.join(valstr))
            rowstr.append(' ')
        listtowrite.append(''.join(rowstr))
    with open(r'2018/day22/output.txt', 'w') as f:
        f.write('\n'.join(listtowrite))


def update_grid(limit,lastupdate):
    updatelist = []
    updated = False
    for p in lastupdate:
        for t in mgrid[p[1]][p[0]].keys():
            if mgrid[p[1]][p[0]][t] == -1:
                continue
            else:
                newlist, updated =update_neighbors(p[0], p[1], t, limit)
                updatelist.extend(newlist)
                    
    return list(set(updatelist)), updated


def update_neighbors(x, y, t, limit):
    currcost = mgrid[y][x][t]
    updatelist = []
    updated = False
    for a in adj:
        if y+a[1]<0 or x+a[0]<0 or y+a[1]>=len(mgrid) or x+a[0]>=len(mgrid[0]):
            continue
        nb = mgrid[y+a[1]][x+a[0]]
        for nbt in nb.keys():
            if nbt not in mgrid[y][x].keys():
                continue
            costtomove = currcost + 1 + cost(t, nbt)
            if (nb[nbt] == -1 or nb[nbt] > costtomove) and costtomove <= limit:
                mgrid[y+a[1]][x+a[0]][nbt] = costtomove
                if (x+a[0], y+a[1]) not in updatelist:
                    updatelist.append((x+a[0], y+a[1]))
                updated = True
            elif (nb[nbt] == -1 and costtomove > limit):
                if (x, y) not in updatelist:
                    updatelist.append((x,y))
    return updatelist, updated
            
def cost(t1, t2):
    if t1 == t2:
        return 0
    else:
        return 7


grid = []

padx, pady = 200,200
for y in range(target[1]+pady):
    grid.append([-1 for x in range(target[0]+padx)])
grid[0][0] = ((0 + depth) % 20183) 
grid[target[1]][target[0]] = ((0 + depth) % 20183) 
for x in range(len(grid[0])):
    erosion((x, 0))
for y in range(len(grid)):
    erosion((0, y))

next_to_calc = {(1,1)}
while next_to_calc:
    next_points = set()
    for p in next_to_calc:
        if grid[p[1]][p[0]] != -1:
            continue
        erosion(p)
        if p[1]+1 < len(grid):
            next_points.add((p[0], p[1]+1))
        if p[0]+1 < len(grid[0]):
            next_points.add((p[0]+1, p[1]))
    next_to_calc = next_points

tgrid = []
tsum = 0
tgrid = []
tsum = 0
for y in range(0, len(grid)):
    row = []
    for x in range(0, len(grid[0])):
        row.append(grid[y][x] % 3)
        tsum += row[-1]
    tgrid.append(row)

## Part 2: find shortest path to target ## 

tooldict = {0: {'c','t'}, 1: {'c', 'n'}, 2: {'t', 'n'}, 8: {'t'}}
#tgrid[target[1]][target[0]] = 8
adj = [(-1,0),(1,0),(0,1),(0,-1)]

# each x, y has a dict with keys of tool options and values of minimum time required to reach
mgrid = []
for y in range(0, len(tgrid)):
    row = []
    for x in range(0, len(tgrid[0])):
        d = {}
        for t in tooldict[tgrid[y][x]]:
            d[t] = -1
        row.append(d)
    mgrid.append(row)
    
limit = 1
updated = True
mgrid[0][0]['t'] = 0
mgrid[0][0]['c'] = 7

lastupdate = [(0,0)]
while mgrid[target[1]][target[0]]['c'] == -1 or mgrid[target[1]][target[0]]['t'] == -1:
    updated = True
    while updated:
        lastupdate, updated = update_grid(limit, lastupdate)
    # print(limit, len(lastupdate))
    #drawm(mgrid)
    limit+=1

print(mgrid[target[1]][target[0]])

