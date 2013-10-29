import itertools

possibles = list(itertools.combinations([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],4))

greatest_n = 0
abcd = []
results = [0]*3025
for com in possibles:
    n = 0
    for i in xrange(0,3025):
        results[i] = 0
    first_level = []
    for j in xrange(0,4):
        for i in xrange(j+1,4):
            p = com[j]
            px = com[i]
            first_level.append([[p,px],p+px])
            first_level.append([[p,px],p-px])
            first_level.append([[p,px],px-p])
            first_level.append([[p,px],p*px])
            if px:
                first_level.append([[p,px],p/px])
            first_level.append([[p,px],px/p])
    second_level = []
    end = len(first_level)
    for j in xrange(0,4):
        for i in xrange(0,end):
            p = com[j]
            if p in first_level[i][0]:
                continue
            px0 = first_level[i][0]
            px1 = first_level[i][1]
            second_level.append([[p]+px0,p+px1])
            second_level.append([[p]+px0,p-px1])
            second_level.append([[p]+px0,px1-p])
            second_level.append([[p]+px0,p*px1])
            # # # # # # # # # # # # # #
            # TEST = [p] + px0
            # if p*px1 == 24:
            #     if (2 in TEST) or (3 in TEST) or (4 in TEST):
            #         ...
            # # # # # # # # # # # # # #
            if px1:
                second_level.append([[p]+px0,p/px1])
            if p:
                second_level.append([[p]+px0,px1/p])
    last_level = []
    end = len(second_level)
    for j in xrange(0,4):
        p = com[j]
        for i in xrange(0,end):
            if p in second_level[i][0]:
                continue
            px1 = second_level[i][1]
            # # # # # # # # # # # # # #
            # TEST = second_level[i][0]
            # if px1 == 24:
            #     if (2 in TEST) or (3 in TEST) or (4 in TEST):
            #         print "here"
            #         quit()
            # # # # # # # # # # # # # #
            last_level.append(p+px1)
            last_level.append(p-px1)
            last_level.append(px1-p)
            last_level.append(p*px1)
            if px1:
                last_level.append(p/px1)
            if p:
                last_level.append(px1/p)
    end = len(first_level)
    for j in xrange(0,end):
        p0 = first_level[j][0][0]
        p1 = first_level[j][0][1]
        p2 = first_level[j][1]
        for i in xrange(j+1,end):
            px0 = first_level[i][0]
            if (p0 in px0) or (p1 in px0):
                continue
            px1 = first_level[i][1]
            last_level.append(p2+px1)
            last_level.append(p2-px1)
            last_level.append(px1-p2)
            last_level.append(p2*px1)
            if px1:
                last_level.append(p2/px1)
            if p2:
                last_level.append(px1/p2)
    end = len(last_level)
    for i in xrange(0,end):
        if last_level[i] == int(last_level[i]):
            results[int(last_level[i])] = 1
    for i in xrange(1,3025):
        if results[i] == 0:
            break
    if (i-1) > greatest_n:
        greatest_n = i-1
        abcd = com
        print i-1, com
    # for i in xrange(0,3025):
    #     print i, results[i]
    # break

string = ''
for i in xrange(0,4):
    string += str(int(abcd[i]))
print string
