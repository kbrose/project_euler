from array import *

tri = [0]*51
n = 0

for n in xrange(1,50): #populates first 50 triangular numbers
    tri[n] = int(.5 * n * (n+1))

f = open("p42_text.txt", 'r')
counter = 0

for line in f:
    word = line.rstrip('\r\n')
    total = 0
    for c in word:
        total = total + ord(c) - 64
    if total in tri:
        counter = counter + 1

print counter
