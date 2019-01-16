# rewrite with deque for practice
from collections import deque

with open(r'2018/day9/input.txt', 'r') as f:
    line = f.read()
fields = line.split()
nplayers = int(fields[0])
nmax = int(fields[6])*100

scores = {}
for i in range(1, nplayers+1):
    scores[i] = 0
player = 1
circ = deque([])
curpos = 0
marb = 0


while marb <= nmax:
    if marb != 0 and marb % 23 == 0:
        scores[player] += marb
        curpos -= 7
        if curpos < 0:
            curpos = len(circ) + curpos
        circ.rotate(len(circ) - curpos -1 )
        scores[player] += circ.pop()
        curpos = 0
    else:
        if curpos == len(circ)-1:
            curpos = 1
        else:
            curpos += 2
        circ.rotate(len(circ) - curpos)
        circ.append(marb)
        curpos = len(circ) -1
    if player == nplayers:
        player = 1
    else:
        player += 1
    marb+=1

print(max(scores.values()))
