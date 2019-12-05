#!/usr/bin/env python3

import math

def l(d):
    i = 0
    try:
        while i < len(d):
            if d[i] == 99:
                break
            if d[i] in [1,2]:
                op(d[i:i+4], d, i)
                i += 3
            i += 1
    except Exception as e:
        print(e)
        return d
    return d

def op(o, d, i):
    e = {
        1 : lambda a,b : a + b,
        2 : lambda a,b : a * b,
    }
    r = e[o[0]](d[o[1]],d[o[2]])
    if r == 1202:
        print((o[3], d[o[3]], r, i))
    d[o[3]] = r

# Part 2
def p2(d):
    z = []
    for x in range(100):
      for y in range(100):
        z.append((x,y))
    d3 = []
    for x,y in z:
        d2 = d.copy()
        d2[1] = x
        d2[2] = y
        d3.append((x,y, importlib.reload(advent2).l(d2)))
    return d3
