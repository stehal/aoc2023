infile = "input.txt"

sum = 0
for l in open(infile):
    chars = list(l.strip())
    digits = [c for c in chars if c.isdigit()]
    sum += int(digits[0])*10 + int(digits[-1])
   
print("solution 1", sum)

d = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def find_first(l):
   for n in range(len(l)+1):
        for k in d.keys():
            if k in l[:n]:
                return d[k]

def find_last(l):
   for n in range(len(l)):
        for k in d.keys():
            if k in l[len(l)-1-n:]:
                return d[k]

sum2 = 0
for line in open(infile):
    l = line.strip()
    sum2 += find_first(l)*10 + find_last(l)

print("solution 2",sum2)
    