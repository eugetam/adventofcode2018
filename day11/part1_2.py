input = 8979

import numpy as np

sz=300
arr = np.zeros((sz,sz))
grid = np.indices((sz, sz))
grid[0] = grid[0]+1
grid[1] = grid[1]+1

power = np.multiply(((grid[1] + 10) * grid[0] + input) , (grid[1] + 10) )
power = np.int32(np.mod(power,1000)/100)-5

scores = []
for sz in range(2,30):
    totalpower = np.zeros((300-sz+1, 300-sz+1))
    for x in range(0, 300-sz+1):
        for y in range(0, 300-sz+1):
            totalpower[x, y] = np.sum(power[x:x+sz, y:y+sz])
    maxpower = np.max(totalpower)
    loc = np.where(totalpower == maxpower)
    scores.append([sz, loc, maxpower])
    print([sz, loc, maxpower])

best = max(scores, key=lambda x: x[2])
print('answer', best[1][1]+1, best[1][0]+1, best[0])
