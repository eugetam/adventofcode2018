with open(r'2018/day7/input.txt', 'r') as f:
    lines = f.readlines()

numw = 5
step = -4

#Step A must be finished before step B can begin.
order = []
basis = []
for line in lines:
    fields = line.split()
    before, after = fields[1], fields[7]
    order.append((before, after))
    basis.append(before)
    basis.append(after)
basis = list(set(basis))

def elig(order, base):
    depset = [y for (x,y) in order]
    return [x for x in base if x not in depset ]

class Worker():
    def __init__(self, task):
        self.task = task
        if self.task:
            self.ttc = ord(task)+step
        else:
            self.ttc = 0
    
    def dec(self):
        self.ttc -= 1

done = []
new_base = list(basis)
worklist = []
for i in range(0, numw):
    eligset = elig(order, new_base)
    if eligset:
        doit = min(eligset)
        new_base.remove(doit)
        worklist.append(Worker(doit))
    else:
        worklist.append(Worker(''))

count = 0
while len(done) < len(basis):
    count+=1
    for i in range(0, numw):
        worklist[i].dec()
        if worklist[i].ttc == 0:
            done.append(worklist[i].task)
            order = [(x,y) for (x,y) in order if x!=worklist[i].task]
        if worklist[i].ttc <= 0:        
            eligset = elig(order, new_base)
            if eligset:
                doit = min(eligset)
                new_base.remove(doit)
                worklist[i].task = doit
                worklist[i].ttc = ord(doit)+step
        


print(done, count)
    