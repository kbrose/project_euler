def reverse(n):
    s = str(n)
    return int(s[::-1])

def ispal(n):
    s_front = str(n)
    s_back = s_front[::-1]
    return (s_front == s_back)

counter = 0

for i in xrange(1,10000):
    n = i
    is_lych = 1
    for j in xrange(0,50):
        n = n + reverse(n)
        if ispal(n):
            is_lych = 0
            break
    if is_lych:
        counter += 1

print counter
        
