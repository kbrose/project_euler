num = 3
den = 2
count = 0
for i in xrange(0,1000):
    temp = num
    num = num + (den*2)
    den = temp + den
    if len(str(num)) > len(str(den)):
        count += 1

print count
