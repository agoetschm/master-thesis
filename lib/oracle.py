import math
import numpy as np

def query(sketch, u, v):
    min = math.inf
    for sd in sketch[u]:
        if sd in sketch[v]:
            candidate = sketch[u][sd] + sketch[v][sd]
            if candidate < min:
                min = candidate
    return min


def query_subset(sketch, xs, ys):
    n = len(xs)
    m = len(ys)

    res = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            res[i][j] = query(sketch, xs[i], ys[j])
    return res
