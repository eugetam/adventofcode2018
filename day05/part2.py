with open(r'2018/day5/input.txt','r') as f:
    input = f.read()

def react(input):
    idx = 0
    while idx < len(input)-1:
        if input[idx+1].lower() == input[idx].lower() and input[idx+1] != input[idx]:
            input = input[:idx] + input[idx+2:]
            idx = max(0, idx-1)
        else:
            idx += 1
    return len(input.strip())

alph = 'abcdefghijklmnopqrstuvwxyz'
c_dict = {}
for c in alph:
    temp_input = input.replace(c, '').replace(c.upper(), '')
    reacted = react(temp_input)
    print(f'{c}:  {reacted}')
    c_dict[c] = reacted

print('answer', c_dict[min(c_dict, key=c_dict.get)])