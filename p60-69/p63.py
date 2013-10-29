def num_of_digs(n):
    count = 0
    while n > 0:
        count += 1
        n /= 10
    return count

counter = 1
powers = []
for i in xrange(2,10):
    add = 0
    for p in xrange(1,25):
        if num_of_digs(i**p) == p:
            if not i**p in powers:
                add += 1
            else:
                powers.append(i**p)
    counter += add
print counter
