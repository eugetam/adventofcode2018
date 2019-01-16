with open(r'2018/day2/input.txt', 'r') as f:
    lines = f.readlines()

targetlen = len(lines[0].strip())
for idx, line in enumerate(lines):
    for idx2, line2 in enumerate(lines):
        matcharr = [1 if x == y else 0 for (x, y) in zip(line.strip(), line2.strip())]
        matchsum = sum(matcharr)
        if matchsum == targetlen:
            break
    if matchsum == targetlen:
        break
print(''.join([x for x, y in zip(line, line2) if x==y]))