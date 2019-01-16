# from inspecting register pattern and assembly code from part 1, determined that 
# the value will be the sum of the factors of the large number

val = 10551264

facs = []
for i in range(1, val+1):
    if i in facs:
        break
    if i*int(val / i) == int(val):
        facs.append(int(i))
        facs.append(int(val/i))
    
print(sum(set(facs)))