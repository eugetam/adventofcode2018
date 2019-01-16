# original slow version

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



def drop(source):
    finished = False
    spreadpoints = set()
    for s in source:
        ys = [yc for xc, yc in clay if s[0]==xc and yc > s[1]]
        ys.extend([yc for xc, yc in water if s[0]==xc and yc > s[1]])
        if len(ys) == 0:
            stop = max([yc for xc, yc in clay])
            flow.update([(s[0], yf) for yf in range(s[1], stop+1)])    
            finished = True
        else:
            stop = min(ys) - 1
            spreadpoints.add((s[0], stop))    
            flow.update([(s[0], yf) for yf in range(s[1], stop+1)])
    return spreadpoints
        

def spread(spreadpoints):
    new_source = set()
    for s in spreadpoints:    
        stop = False
        #rend, lend, y, water
        ystep = 0
        iswater = True
        x, y = s[0], s[1]
        while iswater:
            xstep = 0
            while True:
                if ((x+xstep, y+ystep) not in clay and (x+xstep, y+ystep) not in water) and \
                    ((x+xstep, y+ystep+1) in clay or (x+xstep, y+ystep+1) in water):
                    xstep += 1
                if (x+xstep, y+ystep) in clay or (x+xstep, y+ystep) in water:
                    rend = x+xstep-1
                    iswater = True
                    break
                if ((x+xstep, y+ystep+1) not in clay and (x+xstep, y+ystep+1) not in water):
                    rend = x+xstep
                    new_source.add((rend, y+ystep))
                    iswater = False
                    break
            xstep = 0
            while True:
                if ((x+xstep, y+ystep) not in clay and (x+xstep, y+ystep) not in water) and \
                    ((x+xstep, y+ystep+1) in clay or (x+xstep, y+ystep+1) in water):
                    xstep -= 1
                if (x+xstep, y+ystep) in clay or (x+xstep, y+ystep) in water:
                    lend = x+xstep+1
                    break
                if ((x+xstep, y+ystep+1) not in clay and (x+xstep, y+ystep+1) not in water):
                    lend = x+xstep
                    new_source.add((lend, y+ystep))
                    iswater = False
                    break            
            if iswater:
                water.update([(x1, y+ystep) for x1 in range(lend, rend+1)])
                ystep -= 1
            else:
                flow.update([(x1, y+ystep) for x1 in range(lend, rend+1)])
            #print('here')
    return new_source

def draw():
    xs = [xc for xc, yc in clay]
    ys = [yc for xc, yc in clay]
    minx = min(xs)-1
    maxx = max(xs)+1
    miny = 0
    maxy = max(ys)
    listwrite = []
    for y in range(miny, maxy+1):
        row = []
        for x in range(minx,maxx+1):
            if (x,y) in water:
                row.append('~')
            elif (x,y) in clay:
                row.append('#')
            elif (x,y) in flow:
                row.append('|')
            else:
                row.append('.')
        listwrite.append(''.join(row))
    with open(r'2018/day17/output.txt', 'w') as f:
        f.write('\n'.join(listwrite))

water = set()
flow = set()
last_water_len = 100
last_flow_len = 100
count = 0
source = set([(500, 1)])
spreadpoints = set()
finished = False
last_water_len = 99
last_flow_len = 99
while last_water_len != len(water) or last_flow_len !=len(flow):
    last_water_len = len(water)
    last_flow_len = len(flow)
    spreadpoints = drop(source)
    source = spread(spreadpoints)
    count += 1
    if count % 10 == 0:
        print(len((water)))
        print(len(flow.difference(water)))


draw()
print(len((water)))
#print(sorted(list(water)))

print(len(flow.difference(water)))
#print(sorted(list(flow.difference(water))))

#water 34172
#flow 10575
#flow - 4 from top (above scan)
# answer 44743

