# cave making
# puzzle input
depth = 11820
target = (7,782)
 
# test input
# depth = 510
# target = (10,10)

grid = []       # global

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


for y in range(target[1] + 2):
    grid.append([-1 for x in range(target[0]+2)])
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

# draw(grid, True)   

tgrid = []
tsum = 0
for y in range(0, target[1]+1):
    row = []
    for x in range(0, target[0]+1):
        row.append(grid[y][x] % 3)
        tsum += row[-1]
    tgrid.append(row)

#draw(tgrid, True)
print('part 1 answer: ', tsum)


