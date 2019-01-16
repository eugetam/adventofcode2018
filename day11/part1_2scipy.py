# tried using scipy convolve but performance not that much faster. should have optimized with incremental calculation instead.
input = 8979

import numpy as np
import scipy.signal

sz=300
arr = np.zeros((sz,sz))
grid = np.indices((sz, sz))
grid[0] = grid[0]+1
grid[1] = grid[1]+1

power = np.multiply(((grid[1] + 10) * grid[0] + input) , (grid[1] + 10) )
power = np.int32(np.mod(power,1000)/100)-5

scores = []
for sz in range(2,30):
    totalpower = scipy.signal.convolve2d(power, np.ones((sz, sz), dtype=int), mode='valid')
    maxpower = np.max(totalpower)
    loc = np.where(totalpower == maxpower)
    scores.append([sz, loc, maxpower])
    print([sz, loc, maxpower])

best = max(scores, key=lambda x: x[2])
print('answer', best[1][1]+1, best[1][0]+1, best[0])

# maxs = 0
# for s in scores:
#     #print(s[2], maxs)
#     if s[2] > maxs:
#         #print('here')
#         maxs = s[2]
#         best = list([s[0], s[1]])

# print(best)