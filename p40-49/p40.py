from array import *

frac = ""
n = 1

while len(frac) < 1000001:
    frac = frac + str(n)
    n = n + 1

print int(frac[0]) * \
    int(frac[9]) * \
    int(frac[99]) * \
    int(frac[999]) * \
    int(frac[9999]) * \
    int(frac[99999])
