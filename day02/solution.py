infile = "input.txt"

bdic = {"red":12, "green":13, "blue":14}

def all_counts_in_play_ok(balls):
    for ball in balls:
        count, colour = ball.split()
        if int(count) > bdic[colour]:
            return False
    return True

def all_plays_in_game_ok(plays):
    for play in plays:
        balls = play.strip().split(",")
        if not all_counts_in_play_ok(balls):
            return False
    return True

sum=0
for l in open(infile):
    g,plays = l.strip().split(":")
    if all_plays_in_game_ok(plays.split(";")):
        sum += int(g.split()[1])
   
print("solution 1", sum)

def power_of_game(plays):
    allr,allg,allb=[],[],[]
    for play in plays:
        balls = play.strip().split(",")
        r,g,b =counts_for_play(balls)
        allr.append(r)
        allg.append(g)
        allb.append(b)
    return max(allr)*max(allb)*max(allg)
    
def counts_for_play(balls):
    r,g,b=0,0,0
    for ball in balls:
        count, colour = ball.split()
        match colour:
            case "red":
                r = int(count)
            case "green":
                g = int(count)
            case "blue":
                b = int(count)
    return r,g,b

sum2=0
for l in open(infile):
    sum2+= power_of_game(l.strip().split(":")[1].split(";"))

print("solution 2", sum2)
    