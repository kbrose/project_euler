def is_pal(n):
    s = str(n)
    return s == s[::-1]

pals = []
for p in range(1001):
    if is_pal(p):
        pals.append(p)
print pals
