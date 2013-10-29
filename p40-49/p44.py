from array import *

pents = [n * (3*n - 1) / 2 for n in xrange(1,4000)]
pdic = dict.fromkeys(pents)



def sum_diff_pent():
    D = 10000000000
    for i in xrange(1,2000):
        for j in xrange(i+1,3999):
            diff = pents[j] - pents[i]
            summ = pents[i] + pents[j]
            if pdic.has_key(summ) and pdic.has_key(diff):
                if diff < D:
                    D = diff
                    print D
    return D
            
print sum_diff_pent()
