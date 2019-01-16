from copy import deepcopy
with open('2018/day15/input.txt', 'r') as f:
    lines = f.readlines()
adjacent = [ (-1,0), (0,-1), (0,1),  (1,0)]


class Unit():
    def __init__(self, x, y, elf):
        self.x = x
        self.y = y
        self.hitpoints = 200
        self.elf = elf

    @staticmethod
    def _is_in_range(x, y, elf):
        in_range_list = []
        for a in adjacent:
            if  (y+a[1]>=0 and y+a[1]<len(grid) and x+a[0]>=0 and x+a[0]<len(grid[0])):
                if (isinstance(grid[y+a[1]][x+a[0]], Unit) and 
                        grid[y+a[1]][x+a[0]].elf != elf):
                    in_range_list.append(grid[y+a[1]][x+a[0]])

        if in_range_list:
            return True, in_range_list
        return False, in_range_list

    def find_in_range(self):
        found, self.in_range_list = self._is_in_range(self.x, self.y, self.elf)
        return found

    def attack(self):
        self.find_in_range()
        if not self.in_range_list:
            return
        sorted_targets = sorted(self.in_range_list, key=lambda u: (u.hitpoints, u.y, u.x))
        sorted_targets[0].hitpoints -= 3
        if sorted_targets[0].hitpoints <= 0:
            unit_list.remove(sorted_targets[0])
            grid[sorted_targets[0].y][sorted_targets[0].x] = '.'

    def move(self, x, y):
        grid[self.y][self.x] = '.'
        self.x = x
        self.y = y
        grid[self.y][self.x] = self
    
    def _next_step(self, path, found_locs):
        last = path[-1]
        found_idx = []
        new_paths = []
        for adj in adjacent:
            x, y = last[0] + adj[0], last[1] + adj[1]
            if x<0 or y<0 or x>=len(grid[0]) or y>=len(grid) or (x,y) in found_locs:
                continue
            if grid[y][x] == '#':
                continue
            if grid[y][x] == '.':
                temp = deepcopy(path)
                if len(temp)==1:
                    temp.append((x, y))
                else:
                    temp[1] = (x, y)
                new_paths.append(temp)
                found_idx.append(False)
            elif isinstance(grid[y][x], Unit):
                if grid[y][x].elf != self.elf:
                    temp = deepcopy(path)
                    if len(temp)==1:
                        temp.append((x, y))
                    else:
                        temp[1] = (x, y)
                    new_paths.append(temp)
                    found_idx.append(True)
        return new_paths, found_idx

    def find_next_move(self):
        found_paths = []
        pathlist = []
        for a in adjacent:
            if grid[self.y+a[1]][self.x+a[0]] == '.':
                pathlist.append([(self.x+a[0], self.y+a[1])])
        found_locs = []
        while not found_paths and pathlist:
            new_path_list = []
            for path in pathlist:
                new_paths, found_idx = self._next_step(path, found_locs)
                found_paths.extend([p for p, i in zip(new_paths, found_idx) if i])
                new_path_list.extend(new_paths)
            for p in new_path_list:
                if p[-1] not in found_locs:
                    found_locs.append(p[-1])
            if not new_path_list:
                break
            pathlist = []
            for np in new_path_list:
                if np not in pathlist:
                    pathlist.append(np)
        print(len(pathlist), len(found_paths))
        if found_paths:
            sorted_paths = sorted(found_paths, key=lambda x: (x[-1][1], x[-1][0], x[0][1], x[0][0]))
            # print(sorted_paths[0][-1])
            return sorted_paths[0][0]
        else:
            return []    
        

def is_done():
    gobs, elves = False, False
    for row in grid:
        for unit in row:
            if isinstance(unit, Unit) and unit.hitpoints>0:
                if unit.elf:
                    elves = True
                else:
                    gobs = True
            if gobs and elves:
                return False
    return True


def any_reachable_targets(elf):
    found = False
    for y, row in enumerate(grid):
        for x, u in enumerate(row):
            if isinstance(u, Unit) and u.elf != elf:
                for a in adjacent:
                    if (grid[y+a[1]][x+a[0]] == '.'):
                        return True
    

def draw():
    for row in grid:
        rowline = []
        for u in row:
            if isinstance(u, Unit):
                if u.elf:
                    c = 'E'
                else:
                    c = 'G'
            else:
                c = u
            rowline.append(c)
        print(''.join(rowline))

grid = []
unit_list = []
for y, line in enumerate(lines):
    unitrow = []
    for x, c in enumerate(line.strip()):
        if c == 'G':
            u = Unit(x, y, elf=False)
        elif c == 'E':
            u = Unit(x, y, elf=True)
        elif c == '#':
            u = '#'
        elif c.strip() == '':
            break
        else:
            u = '.'
        unitrow.append(u)
        if isinstance(u, Unit):
            unit_list.append(u)
    grid.append(unitrow)
print(len(grid), len(grid[0]))

done = False
rounds = 1
while not done:
    turn_order = sorted(unit_list, key=lambda u: (u.y, u.x))
    for idx, unit in enumerate(turn_order):
        # print(f'round {rounds} unit at {unit.x}, {unit.y}')
        # draw()
        if unit.hitpoints <= 0:
            continue
        if not unit.find_in_range():
            if any_reachable_targets(unit.elf):
                loc = unit.find_next_move()
                if loc:
                    unit.move(loc[0], loc[1])
                    # print(f'moved to {loc}')
        unit.attack()
        # draw()
        # print('here')
        # for u in unit_list:
        #     print(u.x, u.y, u.hitpoints)
        done = is_done()
        if idx != len(turn_order)-1 and done:
            break
    else:
        rounds += 1
        print(rounds)


score = 0
for u in unit_list:
    print(u.elf, u.x, u.y, u.hitpoints)
    score += u.hitpoints
print(rounds, score)

print('answer ', score*(rounds-1))