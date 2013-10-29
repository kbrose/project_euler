end = 3000
N = 8000000

min_diff = N
min_area = 0

for m in xrange(1,3000):
    m2 = m * m
    for n in xrange(1,3000):
        n2 = n * n
        diff = (m2 * n2) + (m2 * n) + (m * n2) + (m * n) - N
        if diff < 0:
            diff = diff * -1
        if diff < min_diff:
            min_diff = diff
            min_area = m * n

print min_area, min_diff
