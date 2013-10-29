import itertools

def test(gon):
    s1 = gon[0] + gon[1] + gon[2]
    if not s1 == gon[3] + gon[2] + gon[4]:
        return 0
    if not gon[5] + gon[4] + gon[6] == s1:
        return 0
    if not gon[7] + gon[6] + gon[8] == s1:
        return 0
    if not gon[9] + gon[8] + gon[1] == s1:
        return 0
    return 1

def concat(gon):
    minn = gon[0]
    mini = 0
    for i in [3,5,7,9]:
        if gon[i] < minn:
            minn = gon[i]
            mini = i
    s0 = str(gon[0]) + str(gon[1]) + str(gon[2])
    s3 = str(gon[3]) + str(gon[2]) + str(gon[4])
    s5 = str(gon[5]) + str(gon[4]) + str(gon[6])
    s7 = str(gon[7]) + str(gon[6]) + str(gon[8])
    s9 = str(gon[9]) + str(gon[8]) + str(gon[1])
    if mini == 0:
        s = s0 + s3 + s5 + s7 + s9
    if mini == 3:
        s = s3 + s5 + s7 + s9 + s0
    if mini == 5:
        s = s5 + s7 + s9 + s0 + s3
    if mini == 7:
        s = s7 + s9 + s0 + s3 + s5
    if mini == 9:
        s = s9 + s0 + s3 + s5 + s7
    return s



perms = (list(itertools.permutations([1,2,3,4,5,6,7,8,9],9)))
possibles = []

for perm in perms:
    pre_gon = [0]*10
    for i in xrange(0,9):
        pre_gon[i] = perm[i]
    for place in [0,3,5,7,9]:
        gon5 = pre_gon
        gon5.insert(place,10)
        if test(gon5):
            possibles.append(concat(gon5))
    

maxx = possibles[0]
for i in xrange(1,len(possibles)):
    if possibles[i] > maxx:
        maxx = possibles[i]
print maxx
