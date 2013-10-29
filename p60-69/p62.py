import itertools

def compress(tup, ind):
    s = ''
    for i in xrange(0,len(tup[ind])):
        s += tup[ind][i]
    return s

def permutes(a,b):
    x = []
    i = 0
    while a > 0:
        x.append(a % 10)
        i += 1
        a /= 10
    y = []
    i = 0
    while b > 0:
        y.append(b % 10)
        i += 1
        b /= 10
    length = len(x)
    if not length == len(y):
        return 0
    for i in xrange(0,length):
        if x[i] in y:
            y[y.index(x[i])] = [-1]
        else:
            return 0
    return 1

def p62(n):
    for log in xrange(1,100):
        hashed_cubes = {}
        possibles = []
        lower_lim = (int((10**log)**(.333333))+1)
        upper_lim = (int((10**(log+1))**(.333333))+1)
        #print lower_lim, upper_lim
        for i in xrange(lower_lim, upper_lim):
            cube = i * i * i
            sorted_cube = ''.join(sorted(str(cube)))
            if sorted_cube in hashed_cubes:
                hashed_cubes[sorted_cube][0] += 1
                if hashed_cubes[sorted_cube][0] == n:
                    possibles.append(sorted_cube)
            else:
                hashed_cubes[sorted_cube] = [1,cube]
        if possibles:
            min = hashed_cubes[possibles[0]][1]
        for i in xrange(0,len(possibles)):
            if hashed_cubes[possibles[i]][0] == n:
                if hashed_cubes[possibles[i]][1] < min:
                    min = hashed_cubes[possibles[i]][1]
        if possibles:
            return min

sol = p62(6)
print sol, int(sol**(float(1)/float(3)))
