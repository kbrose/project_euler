x = 1
for i in range(1,101): x = x*i

sum = 0

while(x > 0):
	sum = sum + (x % 10)
	x = x / 10

print sum