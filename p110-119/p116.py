def main(n): # assumes n > 4
    r_sols = [0]*(n+1) # solutions containing red bricks
    g_sols = [0]*(n+1) # green
    b_sols = [0]*(n+1) # blue
    r_sols[2] = 1
    g_sols[3] = 1
    b_sols[4] = 1
    for m in [[2,r_sols],[3,g_sols],[4,b_sols]]:
        for total_len in range(m[0]+1,n+1):
            for starting_pos in range(total_len - (m[0] - 1)):
                if total_len-(starting_pos + m[0]) < 0:
                    print 'uh oh'
                (m[1])[total_len] += 1 + (m[1])[total_len-(starting_pos + m[0])]
    return r_sols[n] + g_sols[n] + b_sols[n]

print main(50)
