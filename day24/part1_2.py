import re
from copy import deepcopy
with open(r'2018/day24/input.txt', 'r') as f:
    lines = f.readlines()

targetwin = 'immu'   # put 'any' for part1, 'immu' for part2

class Group():
    def __init__(self, army, id, units, hitpoints, weak, immune, attackpower, attack, initiative):
        self.army = army
        self.id = id
        self.units = units
        self.hitpoints = hitpoints
        self.weak = weak
        self.immune = immune
        self.attackpower = attackpower
        self.attack = attack
        self.initiative = initiative
        
    def eff_power(self):
        return self.units * self.attackpower

    def target(self, t):
        self.chosen_target = t

    def take_attack(self, a):
        if a.attack in self.weak:
            damage = a.eff_power()*2
        elif a.attack in self.immune:
            damage = 0
        else:
            damage = a.eff_power()
        self.units -= damage // self.hitpoints


def isdone(groups):
    ''' done if one army is dead or battle in stalemate '''
    immu=False
    inf=False
    immuattacklist = []
    infattacklist = []
    lefttodo = False
    for g in groups:
        if g.army == 'immu' and g.units>0:
            immu = True
            immuattacklist.append((g.attack, g.eff_power()))
        if g.army == 'inf' and g.units>0:
            inf = True
            infattacklist.append((g.attack, g.eff_power()))
        
    for g in groups:
        if g.army == 'immu' and g.units>0:
            for ia in infattacklist:
                if ia[0] not in g.immune and ia[1]>=g.hitpoints:
                    lefttodo = True
                    break
        if g.army == 'inf' and g.units>0:
            for ia in immuattacklist:
                if ia[0] not in g.immune and ia[1]>=g.hitpoints:
                    lefttodo = True
                    break
        if lefttodo:
            break
    if (not immu or not inf or not lefttodo):
        return True
    else:
        return False


def tally_score(groups):
    score_dict = {'immu':0, 'inf':0}
    for g in groups:
        if g.units>0:
            score_dict[g.army] += g.units
    if score_dict['immu']>0 and score_dict['inf']:
        winner = 'draw'
    elif score_dict['inf']>0:
        winner = 'inf'
    else:
        winner = 'immu'
    return winner, score_dict.get(winner, 0)


# parse input and build armies
id_dict = {'immu':1, 'inf':1}
orig_groups = []
for line in lines:
    if 'Immune System' in line:
        army = 'immu'
    elif 'Infection' in line:
        army = 'inf'
    else:
        result = re.match(r'(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) (\w+) damage at initiative (\d+)', line)
        if result:
            units, hitpoints, weak, attackpower, attack, initiative = result.groups()
            weakfields = weak.replace(',',' ').replace(';','').replace('(','').replace(')','').strip().split()
            immus = []
            weaks = []
            for f in weakfields:
                if f=='immune':
                    s = 'immu'
                    continue
                elif f =='weak':
                    s = 'weak'
                elif f=='to':
                    continue
                else:
                    if s == 'immu':
                        immus.append(f)
                    elif s == 'weak':
                        weaks.append(f)
            orig_groups.append(Group(army, id_dict[army], int(units), int(hitpoints), weaks, immus, int(attackpower), attack, int(initiative)))
            id_dict[army]+=1

for g in orig_groups:
    print(g.army, g.units, g.eff_power())

# increment boost until immunity wins
boost = 0
winner = 'inf'
while winner != targetwin:
    groups = deepcopy(orig_groups)
    for g in groups:
        if g.army == 'immu':
            g.attackpower += boost
    done = False
    while not done:
        targetorder = sorted(groups, key=lambda x: (x.eff_power(), x.initiative), reverse=True)
        chosen = []
        for ag in targetorder:
            ag.target('')
            besttarget = []
            for tg in targetorder:
                if ag == tg or tg in chosen or ag.army==tg.army or ag.units<=0 or tg.units<=0:
                    continue
                if ag.attack in tg.immune:
                    continue
                if ag.attack in tg.weak:
                    damage = 2*ag.eff_power()
                else:
                    damage = ag.eff_power()
                if not besttarget:
                    besttarget = [tg, damage]
                else:
                    if damage > besttarget[1]:
                        besttarget = [tg, damage]
                    elif damage == besttarget[1]:
                        if tg.eff_power() > besttarget[0].eff_power():
                            besttarget = [tg, damage]
                        elif tg.eff_power() == besttarget[0].eff_power():
                            if tg.initiative > besttarget[0].initiative:
                                besttarget = [tg, damage]
            if besttarget:
                chosen.append(besttarget[0])
                ag.target(besttarget[0])
        
        attackorder = sorted(groups, key=lambda x: x.initiative, reverse=True)        
        for ag in attackorder:
            if ag.units <=0 or not ag.chosen_target :
                continue
            ag.chosen_target.take_attack(ag)
        done = isdone(groups)    
    winner, score = tally_score(groups)
    if targetwin == 'any':
        break
    boost += 1
    winner, score = tally_score(groups)

print('final result:',  winner, score)
print(boost)