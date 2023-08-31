# -*- coding: utf-8 -*-

import numpy as np


def beta_om(r: np.ndarray, rA: float) -> np.ndarray:
    """Gives the Osipkov-Merritt beta (velocity anisotropy) profile.
    >>> print(type(beta_om(r=np.array(list(range(5))), rA=1.20)))
    <class 'numpy.ndarray'>
    >>> print(beta_om(r=np.array(list(range(5))), rA=1.20))
    [0.         0.40983607 0.73529412 0.86206897 0.91743119]
    """
    return 1. / (1. + (rA / r) ** 2)


def gamma(dlogrho: np.ndarray, dlogr: np.ndarray) -> np.ndarray:
    return dlogrho / dlogr


def kappa(dlogsigr: np.ndarray, dlogr: np.ndarray) -> np.ndarray:
    return dlogsigr / dlogr


def main():
    import doctest
    doctest.testmod()
    # beta_om()
    # gamma()
    # kappa()


if __name__ == "__main__":
    main()
