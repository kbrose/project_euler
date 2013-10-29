import sys
from sys import argv
from array import *
puzzles = open(argv[1])

def same_row(next_num,j):
    return (next_num/9 == j/9)
def same_col(next_num,j):
    return (next_num-j) % 9 == 0
def same_block(next_num,j):
    return (next_num/27 == j/27 and (next_num % 9)/3 == (j % 9)/3)

def recurse(a):
    next_num = a.find('0')
    if next_num == -1:
        return [1,a]
    excluded_numbers = set()
    for j in range(81):
        if same_row(next_num,j) or same_col(next_num,j) or same_block(next_num,j):
            excluded_numbers.add(a[j])
    for m in '123456789':
        if m not in excluded_numbers:
            res = recurse(a[:next_num]+m+a[next_num+1:])
            if res[0] == 1:
                return res
    return [0,a]

s = 0
for puzzle_num in xrange(50):
    puzzles.readline()
    input = ''
    for i in xrange(9):
        input += (puzzles.readline()).rstrip()
    res = recurse(input)
    print '\t',puzzle_num+1
    s += int(res[1][0]+res[1][1]+res[1][2])
    for i in xrange(9):
        for j in xrange(9):
            print res[1][i*9+j],
        print ''
    print '\n\n'
print s
