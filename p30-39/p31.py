counter = 0

for p1 in xrange(0,201):
    for p2 in xrange(0,201, 2):
        if (p1+p2) > 200:
            break
        for p5 in xrange(0,201, 5):
            if (p1+p2+p5) > 200:
                break
            for p10 in xrange(0,201, 10):
                if (p1+p2+p5+p10) > 200:
                    break
                for p20 in xrange(0,201, 20):
                    if (p1+p2+p5+p10+p20) > 200:
                        break
                    for p50 in xrange(0,201, 50):
                        for P1 in xrange(0,201, 100):
                            for P2 in xrange(0,201, 200):
                                if (p1+p2+p5+p10+p20+p50+P1+P2) == 200:
                                    counter = counter + 1

print counter
