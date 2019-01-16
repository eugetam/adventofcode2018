with open(r'2018/day12/input.txt', 'r') as f:
    lines = f.readlines()

pad = 10
init = lines[0].split()[2]
state = '.'*pad + lines[0].split()[2] + '.'*400

gens = lines[2:]
gens = [x.strip()[:5] for x in gens if x.strip()[-1] == '#']

print(gens)
num_generations = 300        # set to 20 for part 1, set to 300 for part 2
for i in range(num_generations):     
    new_state = '.' * len(state)
    for gen in gens:
        idx = 0
        while idx < len(state):
            found = state[idx:].find(gen) 
            if found < 0:
                break
            idx += found
            new_state = new_state[:idx+2]+'#' +new_state[idx+3:]
            idx += 1
    state = new_state
    

    points = [y for (x, y) in zip(state, range(-1*pad, len(state)+pad+1)) if x=='#']
    print(i, sum(points))


# found pattern within dumped output and linearly extrapolated to 50 billionth (i = 50B-1)