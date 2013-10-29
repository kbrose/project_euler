from array import *

num_of_trips = {} # 0 means untouched, 1 means touched once, 2 means more than once
for i in xrange(0,1500001):
    num_of_trips[i] = 0
triples = {}

for m in xrange(2,1225):
    for n in xrange(1,m):
        m2 = m*m
        n2 = n*n
        a = m2 - n2
        b = 2*m*n
        c = m2 + n2
        if a > b:
            temp = a
            a = b
            b = temp
        k = 1
        base_perim = a + b + c
        while k*(base_perim) < 1500001:
            L = k*base_perim
            if num_of_trips[L] == 2:
                k += 1
                continue
            if num_of_trips[L] == 0:
                num_of_trips[L] = 1
                triples[L] = [k*a,k*b,k*c]
                k += 1
                continue
            if num_of_trips[L] == 1:
                if triples[L] == [k*a,k*b,k*c]:
                    k += 1
                    continue
                num_of_trips[L] = 2
                k += 1
                continue

counter = 0
for i in xrange(1,1500001):
    if num_of_trips[i] == 1:
        counter += 1
print counter
                
