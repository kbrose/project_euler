from math import log

def main(n):
    pwrs = [[27,3,3]] + [[i**2,i,2] for i in range(4,10)]
    a = []
    while len(a) < n:
        min = get_min(pwrs) #  WARNING: HAS SIDE EFFECTS!
        if works(min):
            a.append(min)
    return a[n-1]

def get_min(pwrs):
    largest_base = (max(pwrs, key=lambda x: x[1]))[1]
    curr = min(pwrs)
    while curr[1]**(curr[2]+1) > 10**(curr[1]-1):
        del(pwrs[pwrs.index(curr)])
        curr = min(pwrs)

    if curr[0] > largest_base + 1 and (largest_base + 1 < 9*(log(curr[0],10))):
        pwrs.append([largest_base + 1, largest_base + 1, 1])
        return [largest_base + 1, largest_base + 1, 1]
    else:
        ret = list(curr)
        pwrs[pwrs.index(curr)] = [curr[0]*curr[1],curr[1],curr[2]+1]
        return ret

def works(m):
    s = 0
    num = m[0]
    while num > 0:
        s += num % 10
        num /= 10
    if s == m[1]:
        return True
    return False

print main(30)
