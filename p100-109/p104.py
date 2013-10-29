from math import log

# sqrt5 = 2.236067977499789696409
# phi = (1 + sqrt5) / 2.0
log_10_phi = 0.20898764024997873
log_sqrt_5 = 0.3494850021680094

def ispan(n):
    digs = [0]*10
    while n > 0:
        if digs[n % 10]:
            return False
        digs[n % 10] = 1
        n = n / 10
    for i in xrange(1,10):
        if digs[i] == 0:
            return False
    return True

# this formula relies on the phi definition from wikipedia, as well as
# log arithmetic to only get the info about the first digits
def first_nine_fib(n):
    temp = n * log_10_phi - log_sqrt_5
    return int(10 ** (temp - int(temp) + 8))

f_n_2 = 1
f_n_1 = 1
f_n = 2
k = 3
done = False
while done == False:
    f_n_2 = f_n_1 % 1000000000
    f_n_1 = f_n % 1000000000
    f_n = (f_n_2 + f_n_1) % 1000000000
    k += 1
    
    if ispan(f_n):
        if ispan(first_nine_fib(k)):
            done = True

print k
    





