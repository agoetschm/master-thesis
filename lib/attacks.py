import numpy as np
import math

import oracle
import similarity
import sketch_pattern

def guess_from_l(sketch, freq, k, ref_subset, candidate_subset, unknown_node, dist_mat_knownledge=1):
    dist_candidate_subset = oracle.query_subset(sketch, candidate_subset, ref_subset)

    # only consider a partial distance matrix
    partial_mask = np.around(np.random.binomial(n=1, p=dist_mat_knownledge, size=(len(candidate_subset), len(ref_subset))))
    partial_dist = np.multiply(partial_mask, dist_candidate_subset)
    # set hidden values to avg
    avg = np.sum(partial_dist, axis=(0,1))/np.sum(partial_mask, axis=(0,1))
    partial_dist = partial_dist + np.multiply(avg, (np.ones((len(candidate_subset), len(ref_subset))) - partial_mask))

    # distance estimate vector
    dist_est = sketch_pattern.distance_estimate_subset(sketch, freq, k/2, np.array([unknown_node]), ref_subset)

    # inverse value and calculate similarity
    inv_partial_dist = np.power(partial_dist, -1)
    inv_dist_est = np.power(dist_est, -1)
    sim = similarity.cosine(inv_partial_dist, inv_dist_est)

    # check if the recovery succeded
    guessed_right = (candidate_subset[np.argmax(sim)] == unknown_node)
    return guessed_right
