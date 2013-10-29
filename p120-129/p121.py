from itertools import combinations

'''
This is why there are 11 ways to win, and not 5.  For each "no" ("n")
below, it can be gotten by however many red discs there are in the bag at that time
so for the first n, there's only one red disc, so only one winning way to do that.
For the second n, there are two red discs in the bag, so there are two ways to win
with that combination of y's and n's.  This continues.
y y y y +1
n y y y +1
y n y y +2
y y n y +3
y y y n +4

WHAT IF n = 5? have to multiply the probs together
y y y y y +1
n y y y y +1
y n y y y +2
y y n y y +3
y y y n y +4
y y y y n +5
n n y y y +2
n y n y y +3
n y y n y +4
n y y y n +5
y n n y y +6
          +8
          +10
          +12
          +15
          +20

'''

def prod(l):
    ret = 1
    for item in l:
        ret *= item
    return ret

def main(n):
    numerator = 1
    l = [i+1 for i in range(n)]
    for length in range(1,(n-1)/2+1):
        for c in combinations(l,length):
            numerator += prod(c)
    denom = 1
    for i in range(2,n+2):
        denom *= i
    return numerator, denom

if __name__ == '__main__':
    ret = main(15)
    print ret[1] / ret[0]
