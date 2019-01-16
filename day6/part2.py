# original answer -- slower
with open(r'2018/day6/input.txt', 'r') as f:
    lines = f.readlines()

temp = [x.split(',') for x in lines]
xs = [int(x[0].strip()) for x in temp]
ys = [int(x[1].strip()) for x in temp]

minx = min(xs)-1
maxx = max(xs)+2
miny = min(ys)-1
maxy = max(ys)+2
safe = 0
for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        tot_d = sum([abs(x-xp) + abs(y-yp) for xp, yp in zip(xs, ys)])
        if tot_d < 10000:
            safe += 1

print(safe)
