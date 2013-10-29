# 97 through 122
import time

f = open('/Users/kevin/Computer Science/project_euler/p59_text.txt', 'r')

#print cipher

def translate(a,b,c):
    length = len(cipher)
    temp = cipher
    place = 1
    for i in xrange(0, length):
        if place == 3:
            temp[i] = chr(int(cipher[i]) ^ c)
            place = 1
            continue
        if place == 2:
            temp[i] = chr(int(cipher[i]) ^ b)
            place = 3
            continue
        temp[i] = chr(int(cipher[i]) ^ a)
        place = 2
    return temp
    
def compress(chr_arr):
    s = ''
    for i in xrange(0, len(chr_arr)):
        s += chr_arr[i]
    return s


for a in xrange(97,123):
    for b in xrange(97,123):
        for c in xrange(97,123):
            cipher = f.readline()
            cipher = cipher.split(',')
            f.seek(0) # sets pointer of file back to beginning
            sol = translate(a,b,c)
            sol = compress(sol)
            if 'God' in sol and 'John' in sol:
                print sol
                s = 0
                for c in sol:
                    s += ord(c)
                print s
                quit()


f.close()
