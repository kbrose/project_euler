from itertools import combinations

f = open("p105_text.txt")

fr = f.readline()
sets = []
while fr:
    fs = (fr.strip()).split()
    for i in range(len(fs)):
        fs[i] = int(fs[i])
    fs.sort()
    sets.append(fs)
    fr = f.readline()
    
def test_rest(set, com):
    ret_set = list(set)
    for num in com:
        del(ret_set[ret_set.index(num)])
    for m in range(1,len(ret_set)+1):
        for s in list(combinations(ret_set, m)):
            if sum(s) == sum(com):
                return False
    return True
    
# sum(B) != sum(C) for non-empty, disjoint subsets B and C
def test_1(s):
    for size in range(1,(len(s) / 2) + 1):
        for c in combinations(s, size):
            if not test_rest(s,c):
                return False
    return True


# If B contains more elements than C then S(B) > S(C).
def test_2(s):
    l = len(s)
    left = 2
    right = l - 1
    while right >= left:
        sum_1 = sum(s[:left])
        sum_2 = sum(s[right:])
        if not sum_1 > sum_2:
            return False
        left += 1
        right -= 1
    return True

spec_sum_sets_sum = 0
for i in range(len(sets)):
    if test_2(sets[i]) and test_1(sets[i]): # reverse order for speed
#         print i, '\t', sets[i]
        spec_sum_sets_sum += sum(sets[i])
# for set in sets:
#     if test_2(set) and test_1(set):
#         spec_sum_sets_sum += sum(set)

print spec_sum_sets_sum
