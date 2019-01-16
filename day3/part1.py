import numpy as np

with open(r'2018/day3/input.txt', 'r') as f:
    lines = f.readlines()

mat = np.zeros((1000,1000))

#5 @ 877,374: 24x10
overlap_dict = {}
for line in lines:
    fields = line.split()
    id_val = int(fields[0][1:])
    from_left, from_top = [int(x) for x in fields[2][:-1].split(',')]
    w, h = [int(x) for x in fields[3].split('x')]
    rect = mat[from_left:from_left+w, from_top:from_top+h]
    new_overlap = np.unique(rect[rect > 0])
    for id_overlap in new_overlap:
        overlap_dict[id_overlap] = True
    if len(new_overlap):
        overlap_dict[id_val] = True
    rect[rect > 0] = -1
    rect[rect == 0] = id_val
    
print(np.sum(mat == -1))
