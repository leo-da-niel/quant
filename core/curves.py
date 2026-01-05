import numpy as np

def discount_factor(rate, t):
    return np.exp(-rate * t)


def linear_interpolation(x, xp, fp):
    return np.interp(x, xp, fp)


def build_zero_curve(times, rates):
    """
    times : array-like (year fractions)
    rates : array-like (zero rates)
    """
    return dict(zip(times, rates))
