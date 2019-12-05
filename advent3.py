MAP = {
    'L' : lambda d, x, y, l : [(x - d, y, l + d) for d in range(1, d+1)],
    'R' : lambda d, x, y, l : [(x + d, y, l + d) for d in range(1, d+1)],
    'U' : lambda d, x, y, l : [(x, y + d, l + d) for d in range(1, d+1)],
    'D' : lambda d, x, y, l : [(x, y - d, l + d) for d in range(1, d+1)],
}

def md(x,y):
    return sum(abs(float(a)-float(b)) for a,b in zip(x,y))
    #eturn sum(abs(a-b) for a,b in zip(x,y))

def c(d1, d2):
    g1 = []
    g2 = []
    g1_ = []
    g2_ = []

    p = (0, 0, 0)
    for x in d1:
        ps = MAP[x[0]](int(x[1:]), p[0], p[1], p[2])
        g1 += ps
        g1_ += [(pn[0], pn[1]) for pn in ps]
        p = ps[-1]

    p = (0, 0, 0)
    for x in d2:
        ps = MAP[x[0]](int(x[1:]), p[0], p[1], p[2])
        ps_ = [(pn[0], pn[1]) for pn in ps]
        g2 += ps
        g2_ += ps_
        p = ps[-1]

        for pi, pn_ in enumerate(ps_):
            if pn_ in g1_:
                pn = ps[pi]
                pn2 = g1[g1_.index(pn_)]
                print(md([0,0], pn2), pn[2] + pn2[2], md([0,0], pn2) + pn[2] + pn2[2], pn, pn2)

    return (g1, g2)



if __name__ == '__main__':
   a = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
   b = 'U62,R66,U55,R34,D71,R55,D58,R83'
   c(a,b)
   a = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
   b = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
   c(a,b)
