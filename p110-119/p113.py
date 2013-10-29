'''
so, the idea here is really that we can use a binary string of length 9+n
(where n is the max number of digits interested in) to represent an increasing
number.  Take the following examples:
11000 -> 00
10100 -> 01
10010 -> 02
10001 -> 03
01100 -> 11
01010 -> 12
01001 -> 13
...
00011 -> 33
The idea behind this is simple.  Keep a counter starting at 0.  For every 0,
increase the counter.  For every 1, output the counter.  Then if we have k zeros and
n ones, then we can represent all numbers that are at most n digits long and have
the digits 0-k in them.  Thus, if we want to count all increasing numbers with
n digits, we simply make k=9.  Then, the number of strings with k zeros and n ones
is n+k choose k.  (We subtract one from the total so as to not include 00)

(n+9 choose 9) - 1                              (1)

The idea is a little more complicated for the decreasing case, as we can 
now have trailing zeros.  In order to handle this, we have to have k=10.  However,
we also want to still be able to have leading zeros, so we also make it convention 
to have any 1s in the beginning (i.e. before any zeros) to represent 0s in the output
and after the first zero, then we start decreasing from our max value (which shall
be 10 normally, 3 for the example below).  We now note that this causes the number
0 to crop up more than once.  For example, 10..01..1 = 110..01..1 = 1..10..01,
however, this will occur exactly n times.  Observe the example below
111000 -> 000 *
110100 -> 002
110010 -> 001
110001 -> 000 *
101100 -> 022
101010 -> 021
101001 -> 020
100110 -> 011
100101 -> 010
100011 -> 000 *
011100 -> 222
011010 -> 221
011001 -> 220
010110 -> 211
010101 -> 210
010011 -> 200
001110 -> 111
001101 -> 110
001011 -> 100
000111 -> 000 *
So then we can see that the formula for this is 

(n+10 choose 10) - 1 - n                        (2)

However, when we add these together, we will double count all the repeated numbers,
i.e. 1111 and 22 and 3333333.  But for each power of 10 (or for each n), there are
exactly nine of these numbers.  Thus, if we wish to calculate the number of 
non-bouncy numbers, the formula is

(n+10 choose 10) + (n+9 choose 9) - 10n - 2     (3)
'''

import operator as op
def nCr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def main(n):
    return nCr(9+n, 9) + nCr(10+n, 10) - 10*n - 2
        
print main(100)
