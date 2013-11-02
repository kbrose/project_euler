import primes as Pr

ps = Pr.primes(100000)
used_primes = []
next_prime = 2

def prod(l):
    return reduce(lambda x,y: x*y, l, 1)

def get_nums(mul_with, nums, limit):
    if mul_with * prod(nums) > limit:
        return []
    if nums == []:
        return [mul_with]
    ret = get_nums(mul_with * (nums[0]), nums[1:], limit)
    i = 2
    while mul_with * nums[0]**i < limit:
        ret += get_nums(mul_with * (nums[0]**i), nums[1:], limit)
        i += 1
    return ret

def E(k, limit):
    sorted_rads = [1]
    curr_possibilities = [[2,[2]], [limit,[limit]]]
    prime_index = 1

    while len(sorted_rads) < k:
        if ps[prime_index] < curr_possibilities[0][0]:
            p = [ps[prime_index]]
            curr_possibilities += map (lambda x: [x[0]*p[0],x[1]+p], curr_possibilities)
            curr_possibilities.sort()
            prime_index += 1
        else:
            p = curr_possibilities[0][1]
            del(curr_possibilities[0])
        sorted_rads += sorted(get_nums(1,p,limit))

    return sorted_rads[k-1]

print E(10000, 100000)

