import argparse
import random
import pickle

import sys
sys.path.append('lib/')

import graph
import das_sarma
import cohen

parser = argparse.ArgumentParser()
parser.add_argument("graph")
parser.add_argument("type", choices=["das_sarma", "cohen"])
parser.add_argument("param", type=int)
args = parser.parse_args()

datadir = "data"
graphfile = "%s/%s.graph" % (datadir, args.graph)
type = args.type
param = args.param
sketchfile = "%s/%s-%s-param%d.sketch" % (datadir, args.graph, type, param)

# load the graph
g = graph.load(graphfile)

# generate the sketches
sketch = None
if type == "das_sarma":
    sketch = das_sarma.sketches(g, param)
else:
    sketch = cohen.sketches(g, param)

# save the sketches
with open(sketchfile, 'wb') as output:
    pickle.dump(sketch, output, pickle.HIGHEST_PROTOCOL)
