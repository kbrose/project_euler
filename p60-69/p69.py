# from array import *
# 
# def log(n):
#     s = 0
#     while n > 0:
#         s+=1
#         n/=10
#     return s
# 
# def main(N):
#     prime_size = 12+log(N)
#     primes = [2,3,5,7,11,13]
#     i = 16
#     while len(primes) < prime_size:
#         is_p = 1
#         for p in primes:
#             if not i % p:
#                 is_p = 0
#                 break
#         if is_p:
#             primes.append(i)
#         i += 1
#     prod = 1
#     i = 0
#     while prod < N:
#         prod_prev = prod
#         prod = prod * primes[i]
#         i += 1
#     return prod_prev
#         
# 
# print main(10000001)

# Just keep multiplying consecutive primes until you go over your limit, there ya go!
