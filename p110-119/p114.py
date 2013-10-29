def main(n):
    sols = [0]*(n+1)
    if n < 3:
        return 1
    sols[3] = 1
    for total_len in range(4,n+1):
        for start_pos in range(0,total_len - 2):
            for l in range(3,total_len - start_pos + 1):
                if total_len - (l + start_pos + 1) < 0:
                    sols[total_len] += 1
                else:
                    sols[total_len] += 1 + sols[total_len - (l + start_pos + 1)]
    return sols[n]+1 # +1 to account for "empty" solution

print main(50)
