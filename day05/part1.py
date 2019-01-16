with open(r'2018/day5/input.txt','r') as f:
    input = f.read()

idx = 0
while idx < len(input)-1:
    if input[idx+1].lower() == input[idx].lower() and input[idx+1] != input[idx]:
        input = input[:idx] + input[idx+2:]
        idx = max(0, idx - 1)
    else:
        idx += 1

with open('output.txt', 'w') as f:
    f.write(input)

print(len(input.strip()))
