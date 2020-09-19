# Exploiting the sketch pattern leakage in the GRECS scheme

Meng et al. [1] introduced the GRECS scheme supporting approximate shortest path queries on an encrypted graph. This repository illustrates a query recovery attack using the sketch pattern leakage which can be learned by the server.

### Commands

- generate a random graph with n vertices and an edge probably p and store it under a given id
  ```
  python generate_graph.py n p name
  # e.g.: python generate_graph.py 1000 0.01 test
  ```
- generate the sketches for a graph, either with the Das Sarma et al. or the Cohen et al. algorithm, and with a given precision parameter (σ or ρ depending on the algorithm)
  ```
  python generate_sketch.py graph {das_sarma,cohen} param
  # e.g.: python generate_sketch.py test cohen 3
  ```
- run the query recovery t times on some existing sketches, with m references vertices and l candidate vertices
  ```
  python query_recovery.py t m l graph {das_sarma,cohen} param
  # e.g.: python query_recovery.py 100 50 20 test cohen 3
  # or  : python query_recovery.py 100 50 40 condmat das_sarma 3
  ```

### References
[1] Xianrui Meng, Seny Kamara, Kobbi Nissim, and George Kollios. GRECS: Graph encryption for approximate shortest distance queries. In Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security, pages 504–517, 2015.
