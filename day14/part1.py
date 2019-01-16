input = 260321

elf = 0
elfi = [0,1]

class Node(object):

    def __init__(self, marb, next_node, prev_node):
        self.marb = marb
        self.next_node = next_node
        self.prev_node = prev_node

    
    def destroy(self):
        self.prev_node.set_next(self.get_next())
        self.next_node.set_prev(self.get_prev())


scores = [3, 7]
whichelf = 0

while len(scores)<input + 10:
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
    
print(''.join([str(x) for x in scores[-10:]]))