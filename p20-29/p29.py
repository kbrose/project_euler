powers = {}
counter = 0

for i in xrange(2,101):
    tempcounter = 0
    for j in xrange(2, 101):
        p = i**j
        if not powers.get(p,0): # the 0 changes the default NO answer from none to 0
            powers[p] = 1
            counter = counter + 1
            #for x in xrange(2,7):
            #     if i == 2**x:
            #         tempcounter = tempcounter + 1
            #         if j == 100:
            #             print i, tempcounter
            #for x in xrange(2, 4):
            #    if i == 3**x:
            #        tempcounter = tempcounter + 1
            #        if j == 100:
            #            print i, tempcounter

print counter
