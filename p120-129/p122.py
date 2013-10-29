class p122:
    def __init__(self):
        self.costs = [0] + [200]*200 # the naive way gives lower bound of 200
        self.path  = [0]*201
        self.max_k = 200

    def get_costs(self, power, depth):
        if power > self.max_k or depth > self.costs[power]:
            return
        self.costs[power] = depth # new best!
        self.path[depth] = power # the path has brought us to power
        for i in range(depth,-1,-1):
            self.get_costs(power + self.path[i], depth + 1)

    def main(self):
        self.get_costs(1,0)
        print sum(self.costs)

    def f(self):
        print 5

if __name__ == '__main__':
    p122().main()

