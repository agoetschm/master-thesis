import numpy as np
import math

def frequency(sketch):
    n = len(sketch)
    freq = np.zeros((n))
    for sk in sketch:
        for sd in sk:
            freq[sd] += 1
    return freq

def distance_estimate(sketch, freq, u, v, D):
    n = len(sketch)
    est = math.inf
    for sd in sketch[u]:
        if sd in sketch[v]:
            candidate = (freq[sd]**(1/D))
            if candidate < est:
                est = candidate
    return est

def distance_estimate_subset(sketch, freq, D, xs, ys):
    n = len(xs)
    m = len(ys)

    est = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            est[i, j] = distance_estimate(sketch, freq, xs[i], ys[j], D)
    return est
