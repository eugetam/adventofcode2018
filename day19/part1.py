import re

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

fs = [addr, addi, muli, mulr, borr, bori, bani, banr, 
    eqri, eqir, eqrr, gtri, gtir, gtrr, seti, setr]
f_dict = {f.__name__:f for f in fs}

with open(r'2018\day19\input.txt', 'r') as f:
    lines = f.readlines()
ipr = int(lines[0].strip().split()[1])
lines = lines[1:]
ins = []
for line in lines:
    result = re.match(r'(\w+)\s+(\d+)\s+(\d+)\s+(\d+)', line.strip())
    ins.append([result.group(1), int(result.group(2)),int(result.group(3)),int(result.group(4))])

reg = [0,0,0,0,0,0]

ip = reg[ipr]
count = 0
while ip < len(lines):
    last0 = list(reg)
    newins = ins[ip]
    # seti 5 0 1
    reg[ipr] = ip
    calc = f_dict[newins[0]](newins[1], newins[2], reg)
    reg[newins[3]] = calc
    ip = reg[ipr]
    ip += 1
    # if reg[0] != last0[0]:
    #     print('unequal', ip, newins, count, reg, last0)
    count += 1
    
print(count)
print(reg)