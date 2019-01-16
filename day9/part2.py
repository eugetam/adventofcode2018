# implemented linked list for original solution
with open(r'2018/day9/input.txt', 'r') as f:
    line = f.read()
fields = line.split()
nplayers = int(fields[0])
nmax = int(fields[6]) * 100

scores = {}
for i in range(1, nplayers + 1):
    scores[i] = 0
player = 1
circle = []
curpos = 0
marb = 0

class Node(object):

    def __init__(self, marb, next_node, prev_node):
        self.marb = marb
        self.next_node = next_node
        self.prev_node = prev_node

    def marb(self):
        return self.marb

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
    
    def get_prev(self):
        return self.prev_node
    
    def set_prev(self, new_prev):
        self.prev_node = new_prev
    
    def destroy(self):
        self.prev_node.set_next(self.get_next())
        self.next_node.set_prev(self.get_prev())


while marb <= nmax:
    if marb!=0 and marb % 23 == 0:
        scores[player] += marb
        curpos -= 7
        for i in range(7):
            node = currnode.get_prev()
            currnode = node
        
        scores[player] += currnode.marb
        nextnode = currnode.get_next()
        currnode.destroy()
        currnode = nextnode
    else:
        if marb == 0:
            currnode = Node(0, None, None)
            currnode.set_next(currnode)
            currnode.set_prev(currnode)
        else:
            prevnode = currnode.get_next()
            nextnode = prevnode.get_next()
            currnode = Node(marb, nextnode, prevnode)
            prevnode.set_next(currnode)
            # print(marb, prevnode)
            nextnode.set_prev(currnode)
    marb += 1
    if player == nplayers:
        player = 1
    else:
        player += 1
    

print(max(scores.values()))
