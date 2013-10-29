def main(M):
    counter = 0
    M2 = 2 * M
    end = M2 + 1
    for w_plus_h in xrange(2,end):
        path_len = (M * M) + (w_plus_h * w_plus_h)
        path_len = path_len**.5
        if int(path_len) == path_len:
            if w_plus_h < M + 2:
                counter += w_plus_h / 2
            else:
                temp = M2 - w_plus_h + 1
                counter += (temp / 2) + (temp % 2)
    return counter

num_of_sols = 0
M = 0
while num_of_sols < 1000000:
    M += 1
    num_of_sols += main(M)
print M, num_of_sols
