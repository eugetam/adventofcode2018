# rewrite -- much faster

with open(r'2018/day17/input.txt', 'r') as f:
    lines = f.readlines()
clay = []
for line in lines:
    fields = line.split()
    if fields[0].startswith('y'):
        ytxt = fields[0].strip().replace(',','').replace('y=','')
        xtxt = fields[1].strip().replace(',','').replace('x=','')
    else:
        ytxt = fields[1].strip().replace(',','').replace('y=','')
        xtxt = fields[0].strip().replace(',','').replace('x=','')
    if '..' in ytxt:
        ends = ytxt.split('..')
        ys = range(int(ends[0]), int(ends[1])+1)
    else:
        ys = [int(ytxt)]
    if '..' in xtxt:
        ends = xtxt.split('..')
        xs = range(int(ends[0]), int(ends[1])+1)
    else:
        xs = [int(xtxt)]
    clay.extend([(x, y) for x in xs for y in ys])

def make_grid():
    xs = [xc for xc, yc in clay]
    ys = [yc for xc, yc in clay]
    minx = min(xs)-1
    maxx = max(xs)+1
    miny = 0
    maxy = max(ys)
    print(minx, maxx, miny, maxy)
    grid = []
    for y in range(miny, maxy+1):
        row = []
        for x in range(minx,maxx+1):
            row.append('.')
        grid.append(row)
    for c in clay:
        grid[c[1]-miny][c[0]-minx] = '#'              
        
    return grid, minx, maxx, miny, maxy

def drop(source):
    spreadpoints = set()
    for s in source:
        ystep = 1
        while s[1]+ystep < len(grid) and grid[s[1]+ystep][s[0]] not in ['#','~']:
            grid[s[1]+ystep][s[0]] = '|'
            ystep += 1
        if s[1]+ystep < len(grid):
            spreadpoints.add((s[0], s[1]+ystep-1))
    return spreadpoints
        

def spread(spreadpoints):
    new_source = set()
    for s in spreadpoints:    
        #rend, lend, y, water
        ystep = 0
        iswater = True
        x, y = s[0], s[1]
        while iswater:
            xstep = 0
            while True:
                if grid[y+ystep][x+xstep] != '#' and  grid[y+ystep][x+xstep] != '~' and \
                    (grid[y+ystep+1][x+xstep] == '#' or  grid[y+ystep+1][x+xstep] == '~'):
                    xstep += 1
                elif grid[y+ystep][x+xstep] == '#' or  grid[y+ystep][x+xstep] == '~':
                    rend = x+xstep-1
                    iswater = True
                    break
                elif grid[y+ystep+1][x+xstep] != '#' and  grid[y+ystep+1][x+xstep] != '~':
                    rend = x+xstep
                    new_source.add((rend, y+ystep))
                    iswater = False
                    break
            xstep = 0
            while True:
                if grid[y+ystep][x+xstep] != '#' and  grid[y+ystep][x+xstep] != '~' and \
                    (grid[y+ystep+1][x+xstep] == '#' or  grid[y+ystep+1][x+xstep] == '~'):
                    xstep -= 1
                elif grid[y+ystep][x+xstep] == '#' or  grid[y+ystep][x+xstep] == '~':
                    lend = x+xstep+1
                    break
                elif grid[y+ystep+1][x+xstep] != '#' and  grid[y+ystep+1][x+xstep] != '~':
                    lend = x+xstep
                    new_source.add((lend, y+ystep))
                    iswater = False
                    break
            if iswater:
                for xloc in range(lend, rend+1):
                    grid[y+ystep][xloc] = '~'
                ystep -= 1
            else:
                for xloc in range(lend, rend+1):
                    grid[y+ystep][xloc] = '|'
            #print('here')
    return new_source

def draw():
    for row in grid:
        print(''.join(row))
    
grid, minx, maxx, miny, maxy = make_grid()
source = set([(500-minx, 0-miny)])
spreadpoints = set([0,0,0])
while len(source)>0 and len(spreadpoints)>0:
    spreadpoints = drop(source)
    source = spread(spreadpoints)
    #draw()

count_flow = 0
start_count = False
for row in grid:
    if '#' in row:
        start_count = True
    if not start_count:
        continue
    for loc in row:
        if loc == '~' or loc == '|':
            count_flow += 1

draw()
print('answer', count_flow)
