import argparse
import igraph
import random

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int)
parser.add_argument("p", type=float)
parser.add_argument("name")
args = parser.parse_args()

n = args.n
p = args.p
filename = "data/%s.graph" % args.name

# generate random graph
g = igraph.Graph()
g.add_vertices(n)
edges = []
for i in range(n):
    for j in range(i+1, n):
        if random.random() < p:
            edges.append((i, j))
g.add_edges(edges)

# save it
g.write_edgelist(filename)
