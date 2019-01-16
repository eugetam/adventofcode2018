with open(r'2018/day2/input.txt', 'r') as f:
    lines = f.readlines()

sum2 = 0
sum3 = 0
twos = False
threes = False
for line in lines:
    for c in line:
        if not twos and line.count(c) == 2:
            sum2 +=1
            twos = True
        if not threes and line.count(c) == 3:
            sum3 +=1
            threes = True
    twos = False
    threes = False
print(sum2 * sum3)