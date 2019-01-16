r0, r1, r2, r3, r5 = 0, 0, 0, 0, 0

# this is the assembly code translated and simplified into python
r0 = 0
r2 = 65536
r3 = 10736359

count = 0
minlist = []
two8 = 2**8
two24 = 2**24
while True:
    
    r3 = (((r3 + (r2 % (two8))) % (two24))*65899) % (two24)
    if not (256 > r2):
        r1 = 0
        r2 = r2//256
    else:
        if r3 in minlist:
            print('part2 answer:', prevr3)
            break
        prevr3 = r3
        minlist.append(r3)
        if r3 == r0:
            break
        else:
            r2 = r3 | 65536
            r3 = 10736359
    count += 1
    if count>100000:
        break
print('count', count)

with open(r'2018/day21/output.txt', 'w') as f:
    f.write('\n'.join([str(x) for x in minlist]))
# Part1 Answer: run in debug, breakpoint at line 20 print and line 22 equality. Read R3 when equality evaluated