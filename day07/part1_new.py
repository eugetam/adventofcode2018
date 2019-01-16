with open(r'2018/day7/input.txt', 'r') as f:
    lines = f.readlines()

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

done = []
new_base = list(basis)
while len(done) < len(basis):
    eligset = elig(order, new_base)
    doit = min(eligset)
    new_base.remove(doit)
    done.append(doit)
    order = [(x,y) for (x,y) in order if x!=doit]

print(''.join(done))
    