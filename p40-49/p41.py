from array import *
import itertools

def isprime(n):
    for i in xrange(2,int(n**.5)+1):
        if not (n % i):
            return 0
    return 1

digits = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

# if the sum of the digits of a number n is divisible by three, then so is n
# due to this, only 1, 4, and 7 digit pandigitals can be prime

def FindPrimePan():
    for a in xrange(7,0,-1):
        num1 = digits[a]
        digits[a] = 0
        for b in xrange(7,0,-1):
            if not digits[b]:
                continue
            num2 = num1 + digits[b]
            digits[b] = 0
            for c in xrange(7,0,-1):
                if not digits[c]:
                    continue
                num3 = num2 + digits[c]
                digits[c] = 0
                for d in xrange(7,0,-1):
                    if not digits[d]:
                        continue
                    num4 = num3 + digits[d]
                    digits[d] = 0
                    for e in xrange(7,0,-1):
                        if not digits[e]:
                            continue
                        num5 = num4 + digits[e]
                        digits[e] = 0
                        for f in xrange(7,0,-1):
                            if not digits[f]:
                                continue
                            num6 = num5 + digits[f]
                            digits[f] = 0
                            for i in xrange(7,0,-1):
                                if not digits[i]:
                                    continue
                                num7 = num6 + digits[i]
                                #print num7
                                if isprime(int(num7)):
                                    print "PRIME:",num7
                                    return
                            if not f == 1:
                                digits[f] = str(f)
                            if f == 1:
                                digits[f] = str(f)
                                if not e == 1:
                                    digits[e] = str(e)
                        if not e == 1:
                            digits[e] = str(e)
                        if e == 1:
                            digits[e] = str(e)
                            if not d == 1:
                                digits[d] = str(d)
                    if not d == 1:
                        digits[d] = str(d)
                    if d == 1:
                        digits[d] = str(d)
                        if not c == 1:
                            digits[c] = str(c)
                if not c == 1:
                    digits[c] = str(c)
                if c == 1:
                    digits[c] = str(c)
                    if not b == 1:
                        digits[b] = str(b)
            if not b == 1:
                digits[b] = str(b)
            if b == 1:
                    digits[b] = str(b)
                    if not a == 1:
                        digits[a] = str(a)
        if not a == 1:
            digits[a] = str(a)

FindPrimePan()

#print list(itertools.permutations([7,6,5,4,3,2,1], 7))

def NicerVersion():
    pandigits7 = list(itertools.permutations([7,6,5,4,3,2,1],7))
    for i in xrange(0,len(pandigits7)):
        num = 0
        for j in xrange(0,7):
            num = num + pandigits7[i][6-j]*(10**(j))
        if isprime(num):
            print "PRIME:",num
            break

NicerVersion()
                                                    
