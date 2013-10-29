import random

lo = 0
hi = 4
counter = [0]*40
curr_place = 0
curr_chance = 0
curr_cc = 0
chance = [0,10,11,24,39, 5,-1,-1,-2,-3,-4,-4,-4,-4,-4,-4]
com_ch = [0,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
double = 0
for i in xrange(1000000):
    roll1 = random.randint(lo,hi)
    roll2 = random.randint(lo,hi)
    if roll1 == roll2:
        double += 1
    else:
        double = 0
    curr_place += (roll1 + roll2)
    curr_place = curr_place % 40
    if double == 3:
        curr_place = 10
    if curr_place == 30: # go to jail
        curr_place = 10
    if curr_place in [7,22,36]: # chance card
        place = chance[curr_chance]
        if place >= 0:
            curr_place = place
        elif place == -1:
            if curr_place == 7:
                curr_place = 15
            elif curr_place == 22:
                curr_place = 25
            elif curr_place == 36:
                curr_place = 5
        elif place == -2:
            if curr_place == 7 or curr_place == 36:
                curr_place = 12
            else:
                curr_place = 28
        elif place == -3:
            curr_place -= 3
        curr_chance += 1
        curr_chance = curr_chance % 16
    if curr_place in [2,17,33]: # community chest
        place = com_ch[curr_cc]
        if place >= 0:
            curr_place = place
        curr_cc += 1
        curr_cc = curr_cc % 16
    counter[curr_place] += 1


max1 = [0,0,0]
max2 = [0,0,0]
max3 = [0,0,0]
for i in xrange(0,40):
    if counter[i] > max1[0]:
        max1[0] = counter[i]
        max1[1] = i
        if i:
            max1[2] = float(counter[i])/10000
counter[max1[1]] = 0
for i in xrange(0,40):
    if counter[i] > max2[0]:
        max2[0] = counter[i]
        max2[1] = i
        if i:
            max2[2] = float(counter[i])/10000
counter[max2[1]] = 0
for i in xrange(0,40):
    if counter[i] > max3[0]:
        max3[0] = counter[i]
        max3[1] = i
        if i:
            max3[2] = float(counter[i])/10000
print max1, max2, max3
#print '\t', max(counter)
