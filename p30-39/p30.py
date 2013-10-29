import math

def SumFifths(n):
    sum = 0
    while(n > 0):
        sum = sum + ((n % 10)**5)
        n = math.floor(n / 10)
    return sum

total = 0
for x in xrange(25,360000):
    sum = SumFifths(x)
    if sum == x:
        total = x + total

print total
