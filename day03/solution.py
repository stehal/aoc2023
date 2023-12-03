from collections import defaultdict
import math

infile = "input.txt"

engine = [list(l.strip()) for l in open(infile)]
width = len(engine[0])
height = len(engine)

combos = []
l = [-1,0,1]
for i in range(3):
    for j in range(3):
        combos.append((l[i], l[j]))

def is_adj(adj, coord):
    return adj[0] + coord[0] < width and adj[0] + coord[0] >= 0 and adj[1] + coord[1]< height and adj[1] + coord[1]>=0


def is_part(digits, coords, engine):
    for coord in coords:
        for adj in combos:
            if is_adj(adj, coord):
                symb = engine[adj[1]+coord[1]][adj[0]+coord[0]]
                if symb != "." and symb.isdigit() == False:
                    return True
    return False

def total_if_is_part(digits, coords, engine, totals):
    if is_part(digits, coords, engine):
        totals.append(int("".join(digits)))

digits,coords,totals = [],[],[]
for y in range(height):
    digits,coords = [],[]
    for x in range(width):
        n = engine[y][x]
        if n.isdigit():
            digits.append(n)
            coords.append([x,y])
        else:
            total_if_is_part(digits, coords, engine, totals)
            digits,coords = [],[]
    total_if_is_part(digits, coords, engine, totals)        
total_if_is_part(digits, coords, engine, totals)

print("solution 1", sum(totals))


def adj_asterisk(digits, coords, engine):
    asterisks = []
    for coord in coords:
        for adj in combos:
            if is_adj(adj, coord):
                y,x = adj[1]+coord[1], adj[0]+coord[0]
                if engine[y][x] == "*":
                    asterisks.append((x,y))
    return asterisks

def add_if_adj(digits,coords, engine, d):
    for a in adj_asterisk(digits, coords, engine):
        d[a].add(int("".join(digits)))

digits,coords= [],[]
d = defaultdict(set) 

for y in range(height):
    digits,coords= [],[]
    for x in range(width):
        n = engine[y][x]
        if n.isdigit():
            digits.append(n)
            coords.append([x,y])
        else:
            add_if_adj(digits,coords, engine, d)
            digits,coords= [],[]
    add_if_adj(digits,coords, engine, d)
    digits,coords= [],[]
        
add_if_adj(digits,coords, engine, d)

print("solution 2", sum([math.prod(value) for key, value in d.items() if len(value) == 2]))
        
    