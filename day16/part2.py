import re
from copy import deepcopy

def addr(A, B, reg):
    return reg[A] + reg[B]

def addi(A, B, reg):
    return reg[A] + B

def mulr(A, B, reg):
    return reg[A] * reg[B]

def muli(A, B, reg):
    return reg[A] * B

def banr(A, B, reg):
    return reg[A] & reg[B]

def bani(A, B, reg):
    return reg[A] & B

def borr(A, B, reg):
    return reg[A] | reg[B]

def bori(A, B, reg):
    return reg[A] | B

def seti(A, B, reg):
    return A

def setr(A, B, reg):
    return reg[A]

def gtir(A, B, reg):
    if A > reg[B]:
        return 1
    else:
        return 0

def gtrr(A, B, reg):
    if reg[A] > reg[B]:
        return 1
    else:
        return 0

def gtri(A, B, reg):
    if reg[A] > B:
        return 1
    else:
        return 0

def eqir(A, B, reg):
    if A == reg[B]:
        return 1
    else:
        return 0

def eqrr(A, B, reg):
    if reg[A] == reg[B]:
        return 1
    else:
        return 0

def eqri(A, B, reg):
    if reg[A] == B:
        return 1
    else:
        return 0

# parse input file into samples
with open(r'2018/day16/input.txt', 'r') as f:
    lines = f.readlines()
rebefore = r'Before:\s+\[(\d+), (\d+), (\d+), (\d+)\]'
reop = r'(\d+) (\d+) (\d+) (\d+)'
reafter = r'After:\s+\[(\d+), (\d+), (\d+), (\d+)\]'
sample = []
tp = []
for line in lines:
    result = re.match(rebefore, line)
    if result:
        before = [int(result.group(1)), 
            int(result.group(2)), 
            int(result.group(3)), 
            int(result.group(4))]
        continue
    result = re.match(reafter, line)
    if result:
        after = [int(result.group(1)), 
            int(result.group(2)), 
            int(result.group(3)), 
            int(result.group(4))]
        sample.append([before, after, op])
        before, after, op = '', '', ''
        continue
    result = re.match(reop, line)
    if result:
        if before == '':
            tp.append([int(result.group(1)), 
            int(result.group(2)), 
            int(result.group(3)), 
            int(result.group(4))])
        op = [int(result.group(1)), 
            int(result.group(2)), 
            int(result.group(3)), 
            int(result.group(4))]

fs = [addr, addi, muli, mulr, borr, bori, bani, banr, 
    eqri, eqir, eqrr, gtri, gtir, gtrr, seti, setr]
fn_dict = {f.__name__:f for f in fs}
countd = {}
for f in fs:
    countd[f.__name__] = 0
count = 0
sol = []
for idx, s in enumerate(sample):
    f_match = []
    for f in fs:
        calc = deepcopy(f(s[2][1], s[2][2], s[0]))
        result = deepcopy(s[0])
        result[s[2][3]] = calc

        if result == s[1]:
            f_match.append(f.__name__)
            countd[f.__name__] += 1
            
    if len(f_match) >= 3:
        count += 1
    sol.append([idx, s[2][0], f_match])

# decode by process of elimination
f_dict = {f.__name__:'' for f in fs}
while '' in f_dict.values():
    for s in sol:
        if len(s[2]) == 1:
            f_dict[s[2][0]] = s[1]
            found_f = s[2][0]
            found_o = s[1]
            break
    # print(f_dict)
    for s in sol:
        if found_f in s[2]:
            s[2].remove(found_f)
        if s[1] == found_o:
            s[1] = -99
            s[2] = []

# use decoded opcodes to run test program
o_dict = {o: f for f, o in f_dict.items()}  # flip k:v to v:k in dict
print((o_dict))
reg = [0,0,0,0]
for o in tp:
    calc = deepcopy(fn_dict[o_dict[o[0]]](o[1], o[2], reg))
    reg[o[3]] = calc

print(reg)
