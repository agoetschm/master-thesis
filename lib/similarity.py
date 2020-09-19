import numpy as np

# returns the cosine similarity between two vectors
def cosine(a, b):
    norm = np.multiply(np.linalg.norm(a, axis=1), np.linalg.norm(b, axis=1))
    return np.einsum('ij,ij->i', a, b)/norm
