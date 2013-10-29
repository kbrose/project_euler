from pandigital import *
import itertools

pans = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9],10))

#for i in xrange(0,len(pans)):
#    print i, pans[i][0]

sum = 0

for i in xrange(362880,3628800): # this is where 0 is no longer first number
    num234 = pans[i][1]*100 + pans[i][2]*10 + pans[i][3]
    num345 = pans[i][2]*100 + pans[i][3]*10 + pans[i][4]
    num456 = pans[i][3]*100 + pans[i][4]*10 + pans[i][5]
    num567 = pans[i][4]*100 + pans[i][5]*10 + pans[i][6]
    num678 = pans[i][5]*100 + pans[i][6]*10 + pans[i][7]    
    num789 = pans[i][6]*100 + pans[i][7]*10 + pans[i][8]
    num890 = pans[i][7]*100 + pans[i][8]*10 + pans[i][9]
    
    if (num234 % 2):
        continue
    if (num345 % 3):
        continue
    if (num456 % 5):
        continue
    if (num567 % 7):
        continue
    if (num678 % 11):
        continue
    if (num789 % 13):
        continue
    if (num890 % 17):
        continue
    num = 0
    for j in xrange(0,10):
        num = num + pans[i][j]*(10**(10-j-1))
    sum = sum + num

print sum
