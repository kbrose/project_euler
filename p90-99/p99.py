

numbers_file = open('p99_text.txt')

nums = [] # contains [BASE, EXPONENT]
rl = numbers_file.readline()
while rl:
    rs = rl.split()
    nums.append([int(rs[0]), int(rs[1])])
    rl = numbers_file.readline()
    
def get_max(p1, p2): # gets the max, assumes p1[1] < p2[1]
    if (p2[0] ** (float(p2[1]) / float(p1[1])) > p1[0]):
        return p2
    else:
        return p1

curr_max_pair = nums[0]

for pair in nums:
    if pair[1] < curr_max_pair[1]:
        curr_max_pair = get_max(pair, curr_max_pair)
    else:
        curr_max_pair = get_max(curr_max_pair, pair)
    
for i in xrange(1000):
    if nums[i] == curr_max_pair:
        print i + 1
        break    
