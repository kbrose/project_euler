MAX = 100000

tris = [n * (n + 1) / 2 for n in xrange(286,MAX)]
pent = [n * (3 * n - 1) / 2 for n in xrange(166,MAX)]
hexs = [n * (2 * n - 1) for n in xrange(144,MAX)]
pdic = dict.fromkeys(pent,1)
hdic = dict.fromkeys(hexs,1)

for t in xrange(286,MAX):
    tri = tris[t]
    if pdic.has_key(tri) and hdic.has_key(tri):
        print tri
        break
