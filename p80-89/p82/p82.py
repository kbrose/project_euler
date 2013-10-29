f = open('p82_text.txt', 'r')

s = 1
matrix = []
while s:
    s = f.readline()
    matrix.append(s)
length = len(matrix)
length -= 1 # gets rid of '' part
for i in xrange(0,length):
    matrix[i] = matrix[i].split(',')
    for j in xrange(0,length):
        matrix[i][j] = int(matrix[i][j])

test = []
for i in xrange(0,length):
    test.append(matrix[i][0])

for j in xrange(length-2,-1,-1):
    curr_min = [matrix[0][j+1]+matrix[0][j],0]
    for i in xrange(0,length):
        if matrix[i][j+1]+matrix[i][j] < curr_min[0]:
            curr_min = [matrix[i][j+1]+matrix[i][j],i]
    start = curr_min[1]
    matrix[start][j] += matrix[i][j+1]
    should_look_up = 1
    should_look_down = 1
    for offset in xrange(1,2*length):
        look_up = start-offset
        look_down = start+offset
        if look_up < 0:
            should_look_up = 0
        if look_down > 79:
            should_look_down = 0
        if should_look_up == 0 and should_look_down == 0:
            break
        if should_look_up:
            if matrix[look_up][j+1] < matrix[look_up+1][j]:
                matrix[look_up][j] += matrix[look_up][j+1]
            else:
                matrix[look_up][j] += matrix[look_up+1][j]
        if should_look_down:
            if matrix[look_down][j+1] < matrix[look_down-1][j]:
                matrix[look_down][j] += matrix[look_down][j+1]
            else:
                matrix[look_down][j] += matrix[look_down-1][j]

for i in xrange(0,length):
    print i, test[i], matrix[i][0]

curr_min = matrix[0][0]
for i in xrange(1,length):
    if matrix[i][0] < curr_min:
        curr_min = matrix[i][0]
print curr_min
