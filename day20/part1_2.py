from copy import deepcopy

with open(r'2018\day20\input.txt', 'r') as f:
    fs = f.read()

if len(fs) > 1000:  # real input
    w,h = 300, 300
else:               # test inputs
    w,h = 30,30
grid = []
for y in range(h):
    grid.append(['?' for x in range(w)])
    
dirdict = {'N':(0,-1), 'E':(1,0), 'S':(0,1), 'W':(-1,0)}

def draw(grid, console):
    listtowrite = []
    for row in grid:
        if console:
            print(''.join(row))
        listtowrite.append(''.join(row))
    return listtowrite

def proceed(slist, idx):
    locallist = deepcopy(slist)
    while True:
        # draw(grid, True)
        if idx >= len(fs):
            return slist, True, idx
        if fs[idx] in dirdict.keys():
            news = []
            step = dirdict[fs[idx]]
            for s in locallist:
                if fs[idx] in ['E', 'W']:
                    grid[s[1] + step[1]][s[0] + step[0]] = '|'
                else:
                    grid[s[1] + step[1]][s[0] + step[0]] = '-'
                grid[s[1] + 2*step[1]][s[0] + 2*step[0]] = '.'
                news.append((s[0] + 2*step[0], s[1] + 2*step[1]))
            locallist = list(set(news))
            idx += 1
        if fs[idx] == '|':
            return locallist, False, idx
        if fs[idx] == ')' or fs[idx] =='$':
            return locallist, True, idx
        elif fs[idx] == '(':
            finished = False
            branchlist = []
            while not finished:
                branch_paths, finished, idx = proceed(locallist, idx+1)
                branchlist.extend(branch_paths)
            idx += 1
            locallist = []
            for s in branchlist:
                locallist.append((s[0], s[1]))
            finished = False


startx, starty = int(w/2), int(h/2)
grid[starty][startx] = 'X'
s, f, i = proceed([(startx, starty)], 1)

listtowrite = draw(grid, False)

with open(r'2018\day20\output.txt', 'w') as f:
    f.write('\n'.join(listtowrite))


# find farthest room
adj = [(-1,0), (1,0), (0,1), (0,-1)]
def increment(pathlist):
    newpaths = []
    for p in pathlist:
        last = p[-1]
        for a in adj:
            if (last[0] + 2*a[0], last[1] + 2*a[1]) in endpoints:
                continue
            if grid[last[1] + a[1]][last[0] + a[0]] == '-' or grid[last[1] + a[1]][last[0] + a[0]] == '|':
                newpaths.append(p + [(last[0] + 2*a[0], last[1] + 2*a[1])])
                endpoints.append((last[0] + 2*a[0], last[1] + 2*a[1]))
                if len(p) > 999:
                    farpoints.add((last[0] + 2*a[0], last[1] + 2*a[1]))
    return newpaths

pathlist = [[(startx, starty)]]
startx, starty = int(w/2), int(h/2)
endpoints = [(startx, starty)]
farpoints = set()
count = 0
while pathlist:
    last_pathlist = pathlist
    pathlist = increment(pathlist)
    # if pathlist:
    #     print(len(pathlist[0]) - 1)
    count += 1
print('part 1:', len(last_pathlist[0]) - 1)
print('part 2:', len(farpoints))