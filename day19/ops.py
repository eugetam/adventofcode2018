
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