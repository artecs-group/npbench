import dpnp as np


def kernel(A, p, r):

    return np.matmul(r, A), np.matmul(A, p)
