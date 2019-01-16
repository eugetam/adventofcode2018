with open(r'2018/day3/input.txt', 'r') as f:
    lines = f.readlines()

#5 @ 877,374: 24x10
mat_dict = {}
conflict_dict = {}
for line in lines:
    fields = line.split()
    id_val = int(fields[0][1:])
    from_left, from_top = [int(x) for x in fields[2][:-1].split(',')]
    w, h = [int(x) for x in fields[3].split('x')]
    for x in range(from_left, from_left+w):
        for y in range(from_top, from_top+h):
            if mat_dict.get((x,y), []):
                conflict_dict[id_val] = True
                for conflict_id in mat_dict[(x,y)]:
                    conflict_dict[conflict_id] = True
                mat_dict[(x, y)].append(id_val)
            else:
                mat_dict[(x, y)] = [id_val]

clean_id = [x for x in range(1, len(lines)+1) if int(x) not in conflict_dict.keys()]
print(clean_id)
