sum = 1
curr = 3

for width in xrange(3,1002,2):
    inc = width - 1
    sum = sum + curr #bottom right
    curr = curr + inc
    sum = sum + curr #bottom left
    curr = curr + inc
    sum = sum + curr #top left
    curr = curr + inc
    sum = sum + curr #top right
    curr = curr + inc + 2

print sum
