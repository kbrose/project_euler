import numpy as np

f = open('p102_text.txt')
fr = f.readline()

triangles = []
while fr:
    fs = (fr.strip()).split(',')
    triangles.append([[int(fs[0]),int(fs[1])],
                     [int(fs[2]),int(fs[3])],
                     [int(fs[4]),int(fs[5])]])
    fr = f.readline()
    
# By using cross products, we can test if two points lie on 
# the same side of a line (if they both point in same direction,
# i.e. their dot product is greater than or equal to zero).  Using this,
# we can test to see if a given point is on the same side of the line AB
# as the third point of the triangle, C.  Permute this, and if they are all true
# then we are good to go.

def cross_product(a,b):
    return a[0]*b[1] - b[0]*a[1]

def same_side(p1,p2,a,b):
    b_minus_a = [b[i] - a[i] for i in range(len(a))]
    p1_minus_a = [p1[i] - a[i] for i in range(len(a))]
    p2_minus_a = [p2[i] - a[i] for i in range(len(a))]
    cross_prod_1 = cross_product(b_minus_a, p1_minus_a)
    cross_prod_2 = cross_product(b_minus_a, p2_minus_a)
    return cross_prod_1 / abs(cross_prod_1) == cross_prod_2 / abs(cross_prod_2)

def in_triangle(p, tri):
    res_1 = same_side(p,tri[0],tri[1],tri[2])
    res_2 = same_side(p,tri[1],tri[0],tri[2])
    res_3 = same_side(p,tri[2],tri[0],tri[1])
    if res_1 == res_2 == res_3 == True:
        return 1
    else:
        return 0

s = 0
for tri in triangles:
    s += in_triangle([0,0], tri)
print s
