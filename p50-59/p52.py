log = 1
t = 0
i = 1

def check(n, mult):
    arr = [0]*10
    temp = n
    while temp > 0:
        index = temp % 10
        if arr[index]:
            return 0
        arr[index] = 1
        temp = temp / 10
    temp = n * mult
    while temp > 0:
        index = temp % 10
        if not arr[index] == 1:
            return 0
        arr[index] = 2
        temp = temp / 10
    return 1
    
while t == 0:
    if i > (10**log)/6:
        i = 10**log
        log += 1
    t = 1
    if not check(i, 2):
        t = 0
    if not check(i, 3):
        t = 0
    if not check(i, 4):
        t = 0
    if not check(i, 5):
        t = 0
    if not check(i, 6):
        t = 0
    i = i + 1

print i-1
