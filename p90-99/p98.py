from array import *
from itertools import *
import numpy as np

words_file = open('p98_text.txt')

words = (words_file.readline()).split(',')
anagrams = []

def is_anagram(w1, w2):
    if not len(w1) == len(w2):
        return False
    if w1 == w1[::-1] == w2: # words are actually same palindrome
        return False
    for c in w1:
        try:
            ind = w2.index(c)
        except ValueError:
            return False
        w2 = w2[:ind] + w2[ind+1:]
    return True

for i in xrange(len(words)):
    for j in xrange(i+1, len(words)):
        if is_anagram(words[i], words[j]):
            anagrams.append([words[i], words[j]])


# squares = [i*i for i in range(1,10000)]

def unique_chars(word):
    chars = []
    for c in word:
        if not c in chars:
            chars.append(c)
    return chars

def get_squares(pair, perm):
    uniq = unique_chars(pair[0])
    n1 = ''
    for c in pair[0]:
        n1 = n1 + (perm[uniq.index(c)])
        
    n2 = ''
    for c in pair[1]:
        n2 = n2 + (perm[uniq.index(c)])
    if (n1[0] == '0' or n2[0] == '0'):
        return 0
    n1 = int(n1)
    n2 = int(n2)
        
    if not is_square(n1):
        return 0
    if not is_square(n2):
        return 0
        
    return max(n1, n2)
    
def is_square(num):
    return int(int(num ** 0.5) ** 2) == num

largest_val = 0
for pair in anagrams:
    for p in permutations('0123456789', len(unique_chars(pair[0]))):
        largest_val = max(largest_val, get_squares(pair, p))
    print pair, largest_val
print largest_val



    

