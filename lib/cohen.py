import numpy as np
import math

def sketches(g, rho):
    print("generating cohen sketches with rho=%d" %rho)
    n = g.vcount()
    sketch = [{} for i in range(n)]
    rank = np.random.permutation(n) # vertex to rank mapping
    rank_perm = [0 for i in range(n)] # rank to vertex
    for i in range(n):
        rank_perm[rank[i]] = i
    # rho iterations
    for k in range(rho):
        print("k", k)
        # for each v in rank order
        i = 0
        for v in rank_perm:
            i += 1
            print("\ri: %d/%d" %(i, n), end="")
            # BFS, skip first since it is v
            bfs = g.bfsiter(v, advanced=True)
            next(bfs)
            for u_vert, d, parent in bfs:
                u = u_vert.index
                if v not in sketch[u]:
                    # check if the rank of v is in the k-th lowest of the sketch of u up to now
                    cnt = 0
                    for sd in sketch[u]:
                        if sketch[u][sd] <= d:
                            if rank[sd] < rank[v]:
                                cnt += 1
                                if cnt >= k+1:
                                    break
                    if cnt < k+1:
                        sketch[u][v] = d
        print("")
    return sketch
