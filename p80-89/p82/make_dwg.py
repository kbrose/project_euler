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

for i in xrange(0,length):
    print matrix[i][0], ',',
quit()

print '#vertices'
for i in xrange(0,length):
    for j in xrange(0,length):
        print '%d:%d' % (i,j)
print '#edges'

for i in xrange(0,length):
    for j in xrange(0,length-1):
        print '%d:%d=>%d:%d,X,%d' % (i,j,i,j+1,matrix[i][j+1])

for j in xrange(1,length-1):
    print '%d:%d=>%d:%d,X,%d' % (0,j,1,j,matrix[1][j])
for j in xrange(1,length-1):
    print '%d:%d=>%d:%d,X,%d' % (length-1,j,length-2,j,matrix[length-2][j])
for i in xrange(1,length-1):
    for j in xrange(1,length-1):
        print '%d:%d=>%d:%d,X,%d' % (i,j,i+1,j,matrix[i+1][j])
        print '%d:%d=>%d:%d,X,%d' % (i,j,i-1,j,matrix[i-1][j])


f.close()
