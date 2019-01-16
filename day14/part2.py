elfi = [0, 1]        # elf index
scores = [3, 7]

while True:
    digsum = scores[elfi[0]] + scores[elfi[1]]

    firstrecipe = int(digsum/10)
    if firstrecipe>0:
        scores.append(firstrecipe)
    scores.append(digsum % 10)

    newi1 = elfi[0] + ((scores[elfi[0]] + 1) % len(scores))
    if newi1 >= len(scores):
        newi1 =  newi1 - len(scores)
    newi2 = elfi[1] + ((1 +scores[elfi[1]]) % len(scores))
    if newi2 >= len(scores):
        newi2 = newi2 - len(scores)
    elfi = [newi1, newi2]

    #2,6,0,3,2,1]: 1,4,7,0,6,1
    #     break
    if scores[-6:] == [2,6,0,3,2,1] or scores[-7:-1] == [2,6,0,3,2,1]:
        break
print(scores[-10:])
#print(len(scores))