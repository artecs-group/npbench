import dpnp as np


def kernel(A, x):

    return (A @ x) @ A
