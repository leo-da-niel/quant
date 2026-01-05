class InterestRateSwap:
    def __init__(self, notional, fixed_rate, payment_times, curve):
        self.notional = notional
        self.fixed_rate = fixed_rate
        self.times = payment_times
        self.curve = curve

    def pv_fixed_leg(self):
        return self.notional * sum(
            self.fixed_rate * self.curve.discount(t)
            for t in self.times
        )

    def pv_floating_leg(self):
        return self.notional * (1 - self.curve.discount(self.times[-1]))

    def pv(self):
        return self.pv_floating_leg() - self.pv_fixed_leg()

    def dv01(self, bump=1e-4):
        bumped_rate = self.fixed_rate + bump
        bumped_swap = InterestRateSwap(
            self.notional, bumped_rate, self.times, self.curve
        )
        return bumped_swap.pv() - self.pv()
def parallel_shift(curve, shift):
    shifted_dfs = [
        df * np.exp(-shift * t)
        for t, df in zip(curve.times, np.exp(curve.log_dfs))
    ]
    return ZeroCurve(curve.times, shifted_dfs)
def bucketed_dv01(curve, swap, bump=1e-4):
    dv01 = {}

    for i, t in enumerate(curve.times):
        bumped_dfs = np.exp(curve.log_dfs).copy()
        bumped_dfs[i] *= np.exp(-bump * t)

        bumped_curve = ZeroCurve(curve.times, bumped_dfs)
        bumped_swap = InterestRateSwap(
            swap.notional, swap.fixed_rate, swap.times, bumped_curve
        )
        dv01[t] = bumped_swap.pv() - swap.pv()

    return dv01
