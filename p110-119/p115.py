def main(m, limit):
    sols = [0]*(m*2)
    sols[m] = 1
    total_len = m+1
    while sols[total_len-1] + 1 < limit:
        if total_len == len(sols) - 2:
            sols = double_list_size(sols)
        for start_pos in range(0,total_len - (m-1)):
            for l in range(m,total_len - start_pos + 1):
                if total_len - (l + start_pos + 1) < 0:
                    sols[total_len] += 1
                else:
                    sols[total_len] += 1 + sols[total_len - (l + start_pos + 1)]
        total_len += 1
    return total_len - 1

def double_list_size(l):
    new = [0]*(2*len(l))
    for i in range(len(l)):
        new[i] = l[i]
    del(l)
    return new

print main(50, 10**6)
