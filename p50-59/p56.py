def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n / 10
    return s

curr_max = 0
for a in xrange(1,100):
    for b in xrange(1,100):
        if digit_sum(a**b) > curr_max:
            curr_max = digit_sum(a**b)

print curr_max
