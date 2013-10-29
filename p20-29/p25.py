import math

first = 1
second = 1
counter = 2

while(math.log10(second) < 999):
	temp = second
	second = first + second
	first = temp
	counter = counter + 1

print counter