from array import *
import itertools

def one_to_x_pan(n):
    flag = 0
    digit = 0
    digs = [0]*10
    while n > 0:
        if digs[n % 10] or (n % 10) == 0:
            return 0
        digs[n % 10] = 1
        n = n / 10
    for i in xrange(1,10):
        if digs[i] == 0:
            if not flag:
                digit = i - 1
            flag = 1
        if digs[i] and flag:
            return 0
    if not flag:
        digit = 9
    return digit

def x_to_y_pan(n,x,y):
    digs = [0]*10
    while n > 0:
        if digs[n % 10] or not (x <= (n % 10) <= y):
            return 0
        digs[n % 10] = 1
        n = n / 10
    for i in xrange(x,y+1):
        if digs[i] == 0:
            return 0
    return 1

def all_x_to_y_pans(x,y):
    if y < x:
        temp = x
        x = y
        y = temp
        del(temp)
    raw = list(itertools.permutations(list(xrange(x,y+1))))
    fixed = []
    place = 0
    for i in xrange(0,len(raw)):
        n = 0
        for j in xrange(0,y-x+1):
            n = n + raw[i][(y-x)-j]*(10**j)
        if not raw[i][0] == 0:
            fixed.append(n)
    return fixed
            

def all_x_to_y_pans_desc(x,y):
    if y < x:
        temp = x
        x = y
        y = temp
        del(temp)
    raw = list(itertools.permutations(list(xrange(y,x-1,-1))))
    fixed = []
    place = 0
    for i in xrange(0,len(raw)):
        n = 0
        for j in xrange(0,y-x+1):
            n = n + raw[i][(y-x)-j]*(10**j)
        if not raw[i][0] == 0:
            fixed.append(n)
    return fixed
