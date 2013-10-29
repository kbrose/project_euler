def main(start, end):
    maxx = 0
    a_0 = int(start**.5)
    for N in xrange(start,end):
        Sf = N ** .5
        Si = int(Sf)
        if Si == Sf:
            a_0 += 1
            continue
        #print N
        a_n = a_0
        res_n_add = -a_0
        res_den = 1
        hPrev2 = 0
        hPrev1 = 1
        hCurr = (a_n*hPrev1) + hPrev2
        kPrev2 = 1
        kPrev1 = 0
        kCurr = (a_n * kPrev1) + kPrev2
        while not (hCurr*hCurr) - (N*kCurr*kCurr) == 1:
            step2_n_mul = res_den
            step2_n_add = -res_n_add
            step2_den = N - (res_n_add * res_n_add)
            a_n = int(step2_n_mul*(Sf+step2_n_add)/float(step2_den))
            res_den = step2_den / step2_n_mul
            res_n_add = step2_n_add - (a_n * res_den)
            hPrev2 = hPrev1
            hPrev1 = hCurr
            hCurr = (a_n*hPrev1) + hPrev2
            kPrev2 = kPrev1
            kPrev1 = kCurr
            kCurr = (a_n * kPrev1) + kPrev2
        if hCurr > maxx:
            maxx = hCurr
            maxD = N
    return maxD

print main(1,10001)
    
    #stuff
