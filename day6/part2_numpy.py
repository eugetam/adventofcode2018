# rewrote afterwards with numpy
import numpy as np
with open(r'2018/day6/input.txt', 'r') as f:
    lines = f.readlines()

temp = [x.split(',') for x in lines]
xs = [int(x[0].strip()) for x in temp]
ys = [int(x[1].strip()) for x in temp]

minx = min(xs)-1
xrang = max(xs)+2 - minx
miny = min(ys)-1
yrang = max(ys)+2 - miny

grid = np.indices((xrang, yrang))

mat_list = []
arr = [abs(grid[0]+minx - xp) + abs(grid[1]+miny - yp) for xp, yp in zip(xs, ys)]
arr_3d = np.stack(arr)
print(np.sum(np.sum(arr_3d, axis=0)<10000))

