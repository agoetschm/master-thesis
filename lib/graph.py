import igraph

def load(file):
    g = igraph.Graph.Read_Ncol(file, directed=False)
    # only use the largest connected component
    conn_subg = g.components().subgraph(0)
    return conn_subg
