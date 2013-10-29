def is_bouncy(n):
    last = n % 10
    n /= 10
    dec = False
    inc = False
    while n > 0:
        curr = n % 10
        if curr < last:
            inc = True
        elif curr > last:
            dec = True
        if dec and inc:
            return True
        last = curr
        n /= 10
    return dec and inc

total_bouncies = 0
i = 99
while 100 * total_bouncies < 99 * i:
    i += 1
    if is_bouncy(i):
        total_bouncies += 1
        
print i, total_bouncies
    
