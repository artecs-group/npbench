import dpnp as np


def azimint_naive(data, radius, npt):
    rmax = np.max(radius)
    res = np.zeros(npt, dtype=np.float64)
    for i in range(npt):
        r1 = rmax * i / npt
        r2 = rmax * (i + 1) / npt
        mask_r12 = np.logical_and((r1 <= radius), (radius < r2))
        values_r12 = data[mask_r12]
        res[i] = np.mean(values_r12)
    return res