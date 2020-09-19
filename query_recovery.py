import argparse
import pickle
import math
import numpy as np

import sys
sys.path.append('lib/')

import graph
import attacks
import sketch_pattern

parser = argparse.ArgumentParser()
parser.add_argument("t", type=int)
parser.add_argument("m", type=int)
parser.add_argument("l", type=int)
parser.add_argument("graph")
parser.add_argument("type", choices=["das_sarma", "cohen"])
parser.add_argument("param", type=int)
args = parser.parse_args()

t = args.t
m = args.m
l = args.l

datadir = "data"
graphfile = "%s/%s.graph" % (datadir, args.graph)
type = args.type
param = args.param
sketchfile = "%s/%s-%s-param%d.sketch" % (datadir, args.graph, type, param)

# load the graph
g = graph.load(graphfile)

# load the sketches
sketchinput = open(sketchfile, "rb")
sketch = pickle.load(sketchinput)
if len(sketch) == 3: # hack to deal with sketch generated with other version
    sketch = sketch[0]

# compute freq and average degree
freq = sketch_pattern.frequency(sketch)
k = g.ecount()*2/g.vcount()

# run the query recovery attack t times
print("running query recovery on %s with l=%d m=%d..." %(args.graph, l, m))
result = []
for i in range(t):
    print("\r%d/%d" %(i+1, t), end="")
    ref_vs = np.random.permutation(g.vs.indices)[:m]
    without_ref_vs = np.setdiff1d(g.vs.indices, ref_vs)
    candidate_vs = np.random.permutation(without_ref_vs)[:l]
    v_to_guess = np.random.choice(candidate_vs)
    guessed_right = attacks.guess_from_l(sketch, freq, k, ref_vs, candidate_vs, v_to_guess)
    result.append(guessed_right)
print("")

success_rate = sum(r for r in result)/t
print("success rate:", success_rate)
