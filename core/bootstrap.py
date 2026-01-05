import numpy as np
from core.discounting import discount_factor

def bootstrap_from_swaps(tenors, swap_rates):
    """
    Assumes:
    - annual fixed leg
    - continuous compounding
    """
    dfs = {}

    for i, T in enumerate(tenors):
        fixed_leg = 0.0

        for t in tenors[:i]:
            fixed_leg += swap_rates[i] * dfs[t]

        df_T = (1.0 - fixed_leg) / (1.0 + swap_rates[i])
        dfs[T] = df_T

    return dfs
