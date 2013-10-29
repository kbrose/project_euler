import itertools

tri = []
sqr = []
pen = []
hex = []
hep = []
oct = []

for i in xrange(1,100000):
    t = (i * (i + 1)) / 2
    if t > 999:
        j = i
        while t < 10000:
            tri.append(t)
            j += 1
            t = (j * (j + 1)) / 2
        break
for i in xrange(1,100000):
    s = i * i
    if s > 999:
        j = i
        while s < 10000:
            sqr.append(s)
            j += 1
            s = j * j
        break
for i in xrange(1,100000):
    p = (i * ((3 * i) - 1)) / 2
    if p > 999:
        j = i
        while p < 10000:
            pen.append(p)
            j += 1
            p = (j * ((3 * j) - 1)) / 2
        break
for i in xrange(1,100000):
    h = (i * (2 * i) - 1)
    if h > 999:
        j = i
        while h < 10000:
            hex.append(h)
            j += 1
            h = (j * ((2 * j) - 1))
        break
for i in xrange(1,100000):
    h = (i * (5 * i) - 3) / 2
    if h > 999:
        j = i
        while h < 10000:
            hep.append(h)
            j += 1
            h = (j * ((5 * j) - 3)) / 2
        break
for i in xrange(1,100000):
    o = (i * (3 * i) - 2)
    if o > 999:
        j = i
        while o < 10000:
            oct.append(o)
            j += 1
            o = (j * ((3 * j) - 2))
        break

def cyc(a,b):
    s1 = str(a)
    s2 = str(b)
    return (s1[2]+s1[3]) == (s2[0]+s2[1])

def test(p1,p2,p3,p4,p5,p6):
    for a in xrange(0,len(p1)):
        for b in xrange(0,len(p2)):
            if cyc(p1[a],p2[b]):
                for c in xrange(0,len(p3)):
                    if cyc(p2[b],p3[c]):
                        for d in xrange(0,len(p4)):
                            if cyc(p3[c],p4[d]):
                                for e in xrange(0,len(p5)):
                                    if cyc(p4[d],p5[e]):
                                        for f in xrange(0,len(p6)):
                                            if cyc(p5[e],p6[f]):
                                                if cyc(p6[f],p1[a]):
                                                    return [a,b,c,d,e,f]
    return 0

res = test(oct,hep,hex,pen,sqr,tri)
if res:
    print oct[res[0]],hep[res[1]],hex[res[2]],pen[res[3]],sqr[res[4]],tri[res[5]]
    print sum([oct[res[0]],hep[res[1]],hex[res[2]],pen[res[3]],sqr[res[4]],tri[res[5]]])

order = list(itertools.permutations([5,4,3,2,1,0],6))
polys = [oct,hep,hex,pen,sqr,tri]

for i in xrange(0,len(order)):
    a = polys[order[i][0]]
    b = polys[order[i][1]]
    c = polys[order[i][2]]
    d = polys[order[i][3]]
    e = polys[order[i][4]]
    f = polys[order[i][5]]
    res = 0
    res = test(a,b,c,d,e,f)
    if res:
        print a[res[0]],b[res[1]],c[res[2]],d[res[3]],e[res[4]],f[res[5]]
        print sum([a[res[0]],b[res[1]],c[res[2]],d[res[3]],e[res[4]],f[res[5]]])
        break
