count = 0
a_0 = 1

for N in xrange(2,10000):
    Sf = N ** .5
    Si = int(Sf)
    if Si == Sf:
        a_0 += 1
        continue
    a_n = a_0
    res_n_add = -a_0
    res_den = 1
    results = []
    while not [a_n,res_n_add,res_den] in results:
        results.append([a_n,res_n_add,res_den])
        step2_n_mul = res_den
        step2_n_add = -res_n_add
        step2_den = N - (res_n_add * res_n_add)
        a_n = int(step2_n_mul*(Sf+step2_n_add)/float(step2_den))
        res_den = step2_den / step2_n_mul
        res_n_add = step2_n_add - (a_n * res_den)
    if (len(results) - results.index([a_n,res_n_add,res_den])) % 2:
        count += 1
    if N == 17:
        print results

print count
