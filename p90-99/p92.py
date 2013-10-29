def sqr_digs(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n /= 10
    return s

N = 10000000

length = sqr_digs(N-1)
arr = [0]*length
arr[1] = 1
arr[89] = 89

def recurse(n):
    if ((n == 1) or (n == 89)):
        return n
    if n < length:
        if arr[n]:
            return arr[n]
    res = recurse(sqr_digs(n))
    if n < length:
        arr[n] = res
    return res

counter = 0

for n in xrange(1,N):
    res = recurse(n)
    if res == 89:
        counter += 1

print counter
