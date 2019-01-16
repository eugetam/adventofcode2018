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
h = len(lines)
w = max([len(line) for line in lines])

class cart():
    def __init__(self, x, y, way):
        self.x = x
        self.y = y
        self.way = way
        self.decision = 0 # 0=left, 1=strt, 2= right

    def advance(self):
        if self.way == '^':
            self.y -= 1
        elif self.way == 'v':
            self.y += 1
        elif self.way == '>':
            self.x += 1
        elif self.way =='<':
            self.x -= 1
        
    def new_way(self):
        track = lines[self.y][self.x]
        if track not in ['|', '-', '\\', '/', '+']:
            if lines[self.y-1].strip():
                track = '|'
            elif lines[self.x-1].strip():
                track = '-'
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
            self.way = turn_dict[(track, self.way)]


def crashed(clist):
    locs = [(c.x, c.y) for c in clist]
    if len(set(locs)) < len(locs):
        return True
    else:
        return False

clist = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in ['v', '^', '<', '>']:
            # print(line, x, y)
            clist.append(cart(x, y, c))

crash = False
count = 0
while crash == False :
    clist.sort(key=lambda k: (k.y, k.x))
    for c in clist:
        c.advance()
        c.new_way()
    crash = crashed(clist)
    count+=1

seen = []
for c in clist:
    if (c.x, c.y) in seen:
        print(c.x, c.y)
    else:
        seen.append((c.x, c.y))
