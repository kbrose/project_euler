# def main(a_min, a_max):
#     s = 0
#     for a in range(a_min, a_max + 1):
#         vals_1 = []
#         n = 0
#         val = ((a-1)**n + (a+1)**n) % (a*a)
#         while val not in vals_1:
#             if val != 2:
#                 vals_1.append(val)
#             n += 1
#             val = ((a-1)**n + (a+1)**n) % (a*a)
#         s += max(vals_1)
# #         vals_2 = []
# #         while vals_1 != vals_2:
# #             if not val == 2:
# #                 vals_2.append(val)
# #             n += 1
# #             val = ((a-1)**n + (a+1)**n) % (a*a)
# #         s += max(vals_1)
#     return s
# 
# print main(3,1000)

'''
This has a much nicer solution than the above brute force above.
If we consider each term separately, then we are inspecting (a+1)**n mod a^2
and (a-1)**n mod a^2.  If we expand this, it becomes abundantly clear that
any terms with degree higher than one can be excluded (since they contribute
precisely zero to the mod).  So, for the (a+1)**n, the only two terms of the
expansion that count are a*n + 1.  For (a-1)**n mod a^2, we either get
a*n - 1 for -a*n + 1 depending on n being even or odd.  Thus, when we add the two
together, we get either 2*a*n, or 2.  If we want to maximize this, then we want
the largest value of 2an still less than a^2:
    2an < a^2
    2n < a
    n < a/2
    
    a EVEN:                         a ODD:
    n = (a-2)/2                     n = (a-1)/2
    2an = 2a((a-2)/2) = a(a-2)      2an = 2a((a-1)/2) = a(a-1)
So then it becomes a simple matter of adding these up.

N.B. a is assumed to be > 3 in the above.
'''
def main(a_min, a_max): # ASSUMES a_min > 3!!!!
    s = 0
    for a in range(a_min + (a_min % 2), a_max+1, 2):
        s += a*(a-2)
    for a in range(a_min + (not (a_min % 2)), a_max+1, 2):
        s += a*(a-1)
    return s

print main(3,1000)
