first_two = set()
first_two.add( ((0,0),(0,0)) )
first_two.add( ((25,1),(25,1)) )
first_two.add( ((25,1),(25,2)) )
first_two.add( ((25,2),(25,2)) )
first_two.add( ((0,0),(25,1)) )
first_two.add( ((0,0),(25,2)) )
for i in range(1,21):
    for j in range(1,21):
        for i2 in range(1,4):
            first_two.add( ((0,0),(i,i2)) )
            first_two.add( ((i,i2),(25,1)) )
            first_two.add( ((i,i2),(25,2)) )
            for j2 in range(1,4):
                first_two.add( tuple(sorted([(i,i2),(j,j2)])) )

counter = 0
for start in first_two:
    s = start[0][0]*start[0][1] + start[1][0]*start[1][1]
    for i in list(range(1,21)) + [25]:
        if s + i*2 >= 100:
            counter += 1
            
print 42336 - counter            
