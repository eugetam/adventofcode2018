
with open(r'2018/day7/input.txt', 'r') as f:
    lines = f.readlines()

#Step W must be finished before step I can begin.
nodes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
currnodes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nodes = 'ABCDEF'
# currnodes = 'ABCDEF'
temp = []
graph = {}
for line in lines:
    words = line.split()
    before, after = words[1], words[7]
    # print(before, after)
    if before in graph.keys():
        graph[before].append(after)
    else:
        graph[before] = [after]
    currnodes = currnodes.replace(after, '')
    temp.append(before)
    temp.append(after)

print(graph)
finallist = []
count = 0
while len(graph):
    minnode = min(currnodes)
    finallist.append(minnode)
    if minnode in graph.keys():
        graph.pop(minnode)
    templist = ''.join([x for x in nodes if x not in finallist and x not in currnodes])
    for k, v in graph.items():
        for node in v:
            templist = templist.replace(node, '')
    currnodes = currnodes + templist
    currnodes = currnodes.replace(minnode, '')
    count += 1

finallist += sorted(currnodes)
print(''.join(finallist))