




from primes import primes

N = (50*(10**6))
p = primes(int((N**.5)+1))
end = len(p)

answers = set()
for i in xrange(0,end):
    p4 = p[i]
    s1 = p4**4
    if s1 >= N:
        break
    for j in xrange(0,end):
        p3 = p[j]
        s2 = s1 + (p3**3)
        if s2 >= N:
            break
        for k in xrange(0,end):
            p2 = p[k]
            s3 = s2 + (p2**2)
            if s3 < N:
                answers.add(s3)
            else:
                break

print len(answers)
