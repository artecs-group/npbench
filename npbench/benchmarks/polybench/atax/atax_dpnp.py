import dpnp as np


def kernel(A, x):

    return np.matmul(np.matmul(A, x), A)
