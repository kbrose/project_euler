f = open('p81_text.txt', 'r')

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

for i in xrange((length-2),-1,-1):
    matrix[(length-1)][i] += matrix[(length-1)][i+1]
    matrix[i][(length-1)] += matrix[i+1][(length-1)]

for i in xrange((length-2),-1,-1):
    for j in xrange(i,-1,-1):
        if matrix[i][j+1] < matrix[i+1][j]:
            matrix[i][j] += matrix[i][j+1]
        else:
            matrix[i][j] += matrix[i+1][j]
        if i == j:
            continue
        if matrix[j][i+1] < matrix[j+1][i]:
            matrix[j][i] += matrix[j][i+1]
        else:
            matrix[j][i] += matrix[j+1][i]

print matrix[0][0]

f.close()
