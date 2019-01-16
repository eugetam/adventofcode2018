with open(r'2018/day6/input.txt', 'r') as f:
    lines = f.readlines()

temp = [x.split(',') for x in lines]
xs = [int(x[0].strip()) for x in temp]
ys = [int(x[1].strip()) for x in temp]

minx = min(xs)-1
maxx = max(xs)+2
miny = min(ys)-1
maxy = max(ys)+2
track = {}
last_set = ()
# while True:
for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        ds = [abs(x-xp) + abs(y-yp) for xp, yp in zip(xs, ys)]
        lowest_ds = [(idx, d) for idx, d in enumerate(ds) if d == min(ds)]
        if len(lowest_ds) == 1:
            track[(x,y)] = lowest_ds[0][0]
        else:
            track[(x,y)] = -1
edge_closest = [closest for coord, closest in track.items() if coord[0]==minx or coord[0]==maxx or coord[1]==miny or coord[1]==maxy]
    
final = sorted([y for x, y in track.items() if y not in edge_closest])
count_dict = {}
for x in final:
    if x in edge_closest:
        continue
    if x in count_dict.keys():
        count_dict[x] += 1
    else:
        count_dict[x] = 1

print([count_dict])
print('answer', count_dict[max(count_dict, key=count_dict.get)])

        

