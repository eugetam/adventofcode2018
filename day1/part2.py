with open(r'2018/day1/input.txt', 'r') as f:
    lines = f.readlines()
numlist = [int(x) for x in lines]

idx = 0
running_sum = 0
found_dict = {}
while True:
    running_sum += numlist[idx]
    if idx + 1 == len(numlist):
        idx = 0
    else:
        idx += 1
    if found_dict.get(running_sum, 0):
        print(running_sum)
        break
    found_dict[running_sum] = 1
