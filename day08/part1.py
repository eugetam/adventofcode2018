with open(r'2018/day8/input.txt', 'r') as f:
    input = f.read()
input = input.split()
meta = []

def parse_node(idx):
    num_nodes = int(input[idx])
    idx+=1
    #print(idx, num_nodes)
    num_meta = int(input[idx])
    idx+=1
    #print(idx, num_meta)
    if num_nodes:
        for i in range(0, num_nodes):
            idx = parse_node(idx)
    meta.extend(input[idx:idx+num_meta])
    idx += num_meta
    return idx

parse_node(0)
meta = [int(x) for x in meta]
print('answer', sum(meta))