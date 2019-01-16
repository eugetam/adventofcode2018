with open(r'2018/day8/input.txt', 'r') as f:
    input = f.read()
input = input.split()


def calc_val(idx_in):
    idx = idx_in
    num_nodes = int(input[idx])
    idx+=1
    num_meta = int(input[idx])
    idx+=1
    val = 0
    if num_nodes:
        node_val = []
        for i in range(0, num_nodes):
            idx, temp_val = calc_val(idx)
            node_val.append(temp_val)
        for i in range(0, num_meta):
            if int(input[idx]) <= len(node_val):
                val += node_val[int(input[idx]) - 1]
            idx += 1
    else:
        temp = [int(x) for x in input[idx:idx + num_meta]]
        val = sum(temp)
        idx += num_meta
    return idx, val

idx = 0
num_nodes = input[idx]
idx += 1
num_meta = input[idx]
idx += 1
root_sum = 0
root_array = []
for i in range(0, int(num_nodes)):
    idx, root_val = calc_val(idx)
    root_array.append(root_val)
for i in range(0, int(num_meta)):
    if int(input[idx]) < len(root_array):
        root_sum += root_array[int(input[idx]) - 1]
    idx += 1
print(root_sum)
# for i in range(0, num_meta):
#     root_sum = val_dict[(0, )]
