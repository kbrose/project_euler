from array import *

def ispan(n):
    digs = [0]*10
    while n > 0:
        if digs[n % 10]:
            return 0
        digs[n % 10] = 1
        n = n / 10
    for i in xrange(1,10):
        if digs[i] == 0:
            return 0
    return 1

def LogPlusOne(n):
    i = 0
    while 10**i <= n:
        i = i + 1
    return i

currmax = 0

for i in xrange(9,10):
    cand = 2
    num = i
    NumOfDigits = LogPlusOne(num)
    while NumOfDigits < 9:
        num = (num * (10**LogPlusOne(i * cand))) + (i * cand)
        NumOfDigits = LogPlusOne(num)
        cand = cand + 1
    if NumOfDigits > 9:
        continue
    if ispan(num):
        if num > currmax:
            currmax = num
        print i, num
for i in xrange(90,100):
    cand = 2
    num = i
    NumOfDigits = LogPlusOne(num)
    while NumOfDigits < 9:
        num = (num * (10**LogPlusOne(i * cand))) + (i * cand)
        NumOfDigits = LogPlusOne(num)
        cand = cand + 1
    if NumOfDigits > 9:
        continue
    if ispan(num):
        if num > currmax:
            currmax = num
        print i, num
for i in xrange(900,1000):
    cand = 2
    num = i
    NumOfDigits = LogPlusOne(num)
    while NumOfDigits < 9:
        num = (num * (10**LogPlusOne(i * cand))) + (i * cand)
        NumOfDigits = LogPlusOne(num)
        cand = cand + 1
    if NumOfDigits > 9:
        continue
    if ispan(num):
        if num > currmax:
            currmax = num
        print i, num
for i in xrange(9000,10000):
    cand = 2
    num = i
    NumOfDigits = LogPlusOne(num)
    while NumOfDigits < 9:
        num = (num * (10**LogPlusOne(i * cand))) + (i * cand)
        NumOfDigits = LogPlusOne(num)
        cand = cand + 1
    if NumOfDigits > 9:
        continue
    if ispan(num):
        if num > currmax:
            currmax = num
        print i, num

print "max found: ", currmax
        
