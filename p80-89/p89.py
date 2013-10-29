f = open('p89_text.txt', 'r')

rom_vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'\n':0}
num_vals = {'0':0,'1':1,'2':2,'3':3,'4':2,'5':1,'6':2,'7':3,'8':4,'9':2}

def read_num(s):
    s_p = 0
    s_t = 0
    prev_size = rom_vals[s[0]]
    end = len(s)
    for i in xrange(0,end):
        curr_size = rom_vals[s[i]]
        if not curr_size == prev_size:
            if curr_size > prev_size:
                s_p -= s_t
            else:
                s_p += s_t
            s_t = 0
        prev_size = curr_size
        s_t += curr_size
    return s_p

def write_num(n):
    total_chars = 0
    if n >= 4000:
        total_chars = 2
    s = str(n)
    for c in s:
        total_chars += num_vals[c]
    return total_chars

def int2roman(number):
    numerals={1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L",
              90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    result=""
    for value, numeral in sorted(numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result

#print int2roman(4330)

s = f.readline()
total_saved = 0
while s:
    total_saved += (len(s)-1)-(write_num(read_num(s)))
    s = f.readline()

print total_saved

f.close()
