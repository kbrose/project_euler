f = open('/Users/kevin/Computer Science/project_euler/p54_text.txt', 'r+')

def getdig(c):
    if c in '23456789':
        return int(c)
    if c == 'T':
        return 10
    if c == 'J':
        return 11
    if c == 'Q':
        return 12
    if c == 'K':
        return 13
    if c == 'A':
        return 14

def rank(player, cards):
    if player == 1:
        offset = 0
    if player == 2:
        offset = 5
    nums = [0]*15 # numbers have correct indices, jack = 11, queen = 12, etc.
    suits = [0]*4 # Hearts, Diamonds, Clubs, Spades
    for i in xrange(0, 5):
        if 'H' in cards[i + offset]:
            suits[0] += 1
        if 'D' in cards[i + offset]:
            suits[1] += 1
        if 'C' in cards[i + offset]:
            suits[2] += 1
        if 'S' in cards[i + offset]:
            suits[3] += 1
        nums[getdig(cards[i + offset][0])] += 1
    max1 = 0
    max1ind = 0
    max1val = 0
    max2 = 0
    max2val = 0
    for i in xrange(2,15):
        if nums[i] > max1:
            max1 = nums[i]
            max1ind = i
            max1val = i
    for i in xrange(2,15):
        if nums[i] > max2 and not i == max1ind:
            max2 = nums[i]
            max2val = i
    four_same = 0
    triple = 0
    one_pair = 0
    two_pair = 0
    full_house = 0
    if max1 == 4:
        four_same = 1
    if max1 == 3:
        triple = 1
    if max1 == 2:
        one_pair = 1
    if max2 == 2:
        if one_pair:
            two_pair = 1
        if triple:
            full_house = 1
    consecs = 0
    if not max1 > 1:
        tempcon = 0
        flag = 0
        for i in xrange(2,15):
            if nums[i] == 0 and tempcon > consecs:
                consecs = tempcon
                tempcon = 0
            if nums[i] == 1:
                tempcon += 1
        if tempcon > consecs:
            consecs = tempcon
    straight = 0
    if consecs == 5:
        straight = 1
    flush = 0
    if 5 in suits:
        flush = 1
    royal_flush = 0
    if straight and (14 in nums):
        royal_flush = 1

    if royal_flush:
        return [10, 14, 13]
    if straight and flush:
        for i in xrange(14,1,-1):
            if nums[i]:
                return [9,i,i-1]
    if four_same:
        for i in xrange(14,1,-1):
            if nums[i] < 4 and nums[i]:
                return [8, max1val, i]
    if full_house:
        if max1val < max2val:
            temp = max1val
            max1val = max2val
            max2val = temp
        return [7, max1val, max2val]
    if flush:
        for i in xrange(14,1,-1):
            if nums[i]:
                for j in xrange(i-1,1,-1):
                    if nums[j]:
                        return [6, i, j]
    if straight:
        for i in xrange(14,1,-1):
            if nums[i]:
                return [5, i, i-1]
    if triple:
        for i in xrange(14,1,-1):
            if nums[i] and nums[i] < 3:
                return [4, max1val, i]
    if two_pair:
        if max1val < max2val:
            temp = max1val
            max1val = max2val
            max2val = temp
        return [3, max1val, max2val]
    if one_pair:
        for i in xrange(14,1,-1):
            if nums[i] and nums[i] < 2:
                return [2, max1val, i]
    for i in xrange(14,1,-1):
        if nums[i]:
            for j in xrange(i-1,1,-1):
                if nums[j]:
                    return [1, i, j]
    
            
# 1 High Card
# 2 One Pair
# 3 Two Pairs
# 4 Three of a Kind
# 5 Straight
# 6 Flush
# 7 Full House
# 8 Four of a Kind
# 9 Straight Flush
# 10 Royal Flush

counter = 0

for x in xrange(0,1000):
    s = f.readline()
    cards = s.rsplit(' ')
    cards[9] = cards[9].strip('\n')
    p1 = rank(1, cards)
    p2 = rank(2, cards)
    for i in xrange(0,3):
        if p1[i] < p2[i]:
            break
        if p1[i] > p2[i]:
            counter += 1
            break

print counter
    

f.close()
