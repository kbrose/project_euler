def main(N):
    place = 0
    hPrev1 = 0
    hCurr = 1
    kPrev1 = 1
    kCurr = 0
    place_two = 0
    for n in xrange(0,N):
        if place == 0:
            place = 1
            a_n = 2
        elif place == 1 or place == 3:
            if place == 1:
                place = 2
            if place == 3:
                place = 1
            a_n = 1
        elif place == 2:
            place_two += 2
            place = 3
            a_n = place_two
        kPrev2 = kPrev1
        kPrev1 = kCurr
        kCurr = (a_n * kPrev1) + kPrev2
        hPrev2 = hPrev1
        hPrev1 = hCurr
        hCurr = (a_n*hPrev1) + hPrev2
    return [hCurr,kCurr]
    
def sum_digs(N):
    count = 0
    while N > 0:
        count += N % 10
        N /= 10
    return count

print sum_digs(main(100)[0])
