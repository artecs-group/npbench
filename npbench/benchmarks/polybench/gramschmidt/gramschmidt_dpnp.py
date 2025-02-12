import dpnp as np


def kernel(A):

    Q = np.zeros_like(A)
    R = np.zeros((A.shape[1], A.shape[1]), dtype=A.dtype)

    for k in range(A.shape[1]):
        nrm = np.dot(A[:, k], A[:, k])
        R[k, k] = np.sqrt(nrm)
        Q[:, k] = A[:, k] / R[k, k]
        for j in range(k + 1, A.shape[1]):
            R[k, j] = np.dot(Q[:, k], A[:, j])
            A[:, j] -= Q[:, k] * R[k, j]
    #     R[k, k+1:] = np.transpose(Q[:, k]) @ A[:, k+1:]
    #     A[:, k+1:] -= Q[:, k] @ R[k, k+1:]
    # nrm = np.dot(A[:, -1], A[:, -1])
    # R[-1, -1] = np.sqrt(nrm)
    # Q[:, -1] = A[:, -1] / R[-1, -1]

    return Q, R
