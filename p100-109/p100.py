# import time
# 
# def main(m,n):
#     while not n * (n-1) == (m * (m-1) / 2):
#         m += 1
#         m_test_term = (m * (m-1) / 2)
#         n = int(0.5 * ((2*m*m - 2*m + 1)**0.5) + 1)
#     return n, m
# 
# m = 1014051306883
# i = 1
# for m in [int( (0.6305958973*(5.803160237**x)) * (0.92909*(1.00679**x)) ) for x in range(1,17)]:
#     start = time.time()
#     a, b = main(m - 1,1)
#     end = time.time()
#     print i, end - start
#     print '\tsol:', a, b, '\n'
#     i = i + 1

# a, b = main(int( (0.6305958973*(5.803160237**16))), 1)
# print a, b

# SEE http://www.alpertron.com.ar/METHODS.HTM#Hyperb for methods

b = 655869061
n = 927538921

while n < 10**12:
    b_next = (3 * b) + (2 * n) - 2
    n_next = (4 * b) + (3 * n) - 3
    b = b_next
    n = n_next

print b, n
    
    
