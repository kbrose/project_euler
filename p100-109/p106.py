from itertools import combinations

def main(n):
    positions = [i+1 for i in range(n)]

    total = 0

    for m in range(2,n):
        matches = list(combinations(positions, m))
        for i in range(len(matches)-1):
            for j in range(i+1, len(matches)):
                if len(list(set(matches[i]) & set(matches[j]))) > 0:
                    continue
                set_1_score = 0
                set_2_score = 0
                set_1 = sorted(matches[i])
                set_2 = sorted(matches[j])
                set_1.reverse()
                set_2.reverse()
                for iter in range(m):
                    if set_1[iter] > set_2[iter]:
                        set_1_score += 1
                    elif set_2[iter] > set_1[iter]:
                        set_2_score += 1
                    else:
                        print "I've made a huge mistake"
                if not 0 in [set_1_score, set_2_score]:
                    total += 1
    return total

# for n in range(3,13):
#     print n, main(n)
print main(12)
