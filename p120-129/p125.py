def is_pal(n):
    s = str(n)
    return s == s[::-1]

def main(n):
    pals = set()
    limit = int(n**0.5)+1
    for start in range(1,limit):
        for end in range(start+2,limit):
            test = sum(map (lambda x: x*x, range(start,end)))
            if test >= n:
                break
            if is_pal(test):
                pals.add(test)
    return sum(pals)

print main(10**8)
