# part 1 code was too slow for part 2 -- see 2 versions of part 2
with open(r'2018/day9/input.txt', 'r') as f:
    line = f.read()
fields = line.split()
nplayers = int(fields[0])
nmax = int(fields[6])

scores = {}
for i in range(1, nplayers+1):
    scores[i] = 0
player = 1
circle = []
curpos = 0
marb = 0
while marb <= nmax:
    if marb != 0 and marb % 23 == 0:
        scores[player] += marb
        curpos -= 7
        if curpos < 0:
            curpos = len(circle) + curpos
    
        # print(marb, len(circle), curpos)
        # print(circle)
        to_remove = circle[curpos]
        scores[player] += to_remove
        circle.remove(to_remove)
        if curpos > len(circle)-1:
            curpos = 0
        # print(circle)
        # print(player, scores[player])
    else:
        if curpos <= len(circle) - 2:
            curpos += 2
            
        else:
            curpos = 1
        new_circle = circle[:curpos]
        new_circle.append(marb)
        new_circle.extend(circle[curpos:])
        circle = new_circle
        # print(marb, circle, curpos)
    marb += 1
    if player == nplayers:
        player = 1
    else:
        player += 1
    

print(max(scores.values()))
