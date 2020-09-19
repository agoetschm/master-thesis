import numpy as np
import math


def sketches(g, sigma, c=1):
    print("generating das sarma sketches with sigma=%d and c=%f" %(sigma, c))
    n = g.vcount()
    r = math.floor(math.log2(n))

    sketch = [{} for _ in range(n)]

    for s in range(sigma):
        print("s", s)
        # iterate set sizes
        for i in range(r+1):
            seeds_set = set(np.random.permutation(n)[:2**i].flat)
            # for each node, get the closest in the seed set
            for v in g.vs.indices:
                print("\ri: %d/%d\tv: %d/%d" %(i, r, v, n), end="")
                for u, d, _ in g.bfsiter(v, advanced=True):
                    if u.index in seeds_set:
                        sketch[v][u.index] = d
                        break
            # countermeasure
            if c > 1:
                if i > r/c:
                    for seed in seeds_set:
                        sd = int(seed)
                        # number of fake seeds to add
                        n_fake = int(n/(2**(r/c)) - n/(2**i))
                        # choose random sketches
                        rand_vs = set(np.random.permutation(n)[:n_fake])
                        # bfs to add the fake vertices
                        for v, d, _ in g.bfsiter(sd, advanced=True):
                            if v.index in rand_vs:
                                sketch[v.index][sd] = d
        print("")
    return sketch
