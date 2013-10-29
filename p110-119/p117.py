# def main(n): # assumes n > 4
#     r_sols = [0]*max((n+1), 5) # solutions starting with red bricks
#     g_sols = [0]*max((n+1), 5) # green
#     b_sols = [0]*max((n+1), 5) # blue
#     r_sols[2] = 1
#     g_sols[3] = 1
#     b_sols[4] = 1
#     for total_len in range(2,n+1):
#         for m in [[2,r_sols],[3,g_sols],[4,b_sols]]:
#             if m[0] >= total_len:
#                 continue
#             for starting_pos in range(total_len - (m[0] - 1)):
#                 (m[1])[total_len] += 1
#                 (m[1])[total_len] += r_sols[total_len-(starting_pos + m[0])]
#                 (m[1])[total_len] += g_sols[total_len-(starting_pos + m[0])]
#                 (m[1])[total_len] += b_sols[total_len-(starting_pos + m[0])]
#     return r_sols[n] + g_sols[n] + b_sols[n] + 1

def main(n):
    if n in [0,1,2,3,4]:
        return [0,1,1,2,4][n]
    n_4 = 1
    n_3 = 1
    n_2 = 2
    n_1 = 4
    i = 4
    while i <= n:
        temp = n_4
        n_4 = n_3
        n_3 = n_2
        n_2 = n_1
        n_1 = temp + n_4 + n_3 + n_2 
        i += 1
    return n_1

for i in range(10):
    print i, main(i)
# print main(50)
