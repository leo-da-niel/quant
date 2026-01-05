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


class ZeroCurve:

    def __init__(self, times, dfs):
        self.times = np.array(times)
        self.log_dfs = np.log(np.array(dfs))

    def discount(self, t):
        log_df = np.interp(t, self.times, self.log_dfs)
        return np.exp(log_df)

    def zero_rate(self, t):
        return -np.log(self.discount(t)) / t
