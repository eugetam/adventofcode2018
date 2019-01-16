with open(r'2018/day13/input.txt', 'r') as f:
    lines = f.readlines()

turn_dict = {
    ('\\','^'): '<',
    ('\\','>'): 'v',
    ('\\','<'): '^',
    ('\\','v'): '>',
    ('/','^'): '>',
    ('/','>'): '^',
    ('/','<'): 'v',
    ('/','v'): '<'
}

left_dict = {
    '^': '<',
    'v': '>',
    '<': 'v',
    '>': '^',
}
right_dict = {
    '^': '>',
    'v': '<',
    '<': '^',
    '>': 'v',
}

class cart():
    def __init__(self, x, y, way):
        self.x = x
        self.y = y
        self.way = way
        self.decision = 0 # 0=left, 1=strt, 2= right
        self.drop = False

    def advance(self):
        if self.way == '^':
            self.y -= 1
        elif self.way == 'v':
            self.y += 1
        elif self.way == '>':
            self.x += 1
        elif self.way =='<':
            self.x -= 1
        else:
            raise Exception()
        
    def new_way(self):
        track = lines[self.y][self.x]
        if track not in ['|', '-', '\\', '/', '+']:
            if track in ['^', 'v']:
                track = '|'
            elif track in ['<', '>']:
                track = '-'
            else: 
                raise Exception()
        if track == '-' or track == '|':
            return
        elif track == '+':
            if self.decision == 0:
                self.way = left_dict[self.way]
                self.decision = 1
            elif self.decision == 1:
                self.way = self.way
                self.decision = 2
            elif self.decision == 2:
                self.way = right_dict[self.way]
                self.decision = 0
            else:
                raise Exception()
        else:
            self.way = turn_dict[(track, self.way)]


def crashed(clist):
    locs = [(c.x, c.y) for c in clist]
    crashlist = []
    for i, loc in enumerate(locs):
        if clist[i].drop:
            continue
        match = [idx for idx, l in enumerate(locs) if l==loc and idx!=i and not clist[idx].drop]
        for m in match:
            crashlist.append([i, m])
    return crashlist


clist = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in ['v', '^', '<', '>']:
#            print(line, x, y)
            clist.append(cart(x, y, c))

crashed_carts = []
count = 0
remaining_carts = len(clist)
while remaining_carts > 1:
    clist.sort(key=lambda k: (k.y, k.x))
    for c in clist:
        c.advance()
        c.new_way()
        crashed_carts = crashed(clist)
        if crashed_carts:
            for crash in crashed_carts:
                clist[crash[0]].drop = True
                clist[crash[1]].drop = True
                print(f'crashed at {clist[crash[0]].x}, {clist[crash[0]].y}')
        remaining_carts = sum([1 for c in clist if not c.drop])
    if remaining_carts <2:
        break
    count+=1
    # print('---', count)

for c in clist:
    if not c.drop:
        print('answer', c.x, c.y, c.way)
print('num rounds', count)