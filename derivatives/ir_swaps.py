class InterestRateSwap:

    def __init__(self, notional, fixed_rate, payment_times, curve):
        self.notional = notional
        self.fixed_rate = fixed_rate
        self.times = payment_times
        self.curve = curve

    def pv_fixed_leg(self):
        pv = 0.0
        for t in self.times:
            df = self.curve.discount(t)
            pv += self.fixed_rate * df
        return self.notional * pv

    def pv_floating_leg(self):
        df_start = self.curve.discount(0.0)
        df_end = self.curve.discount(self.times[-1])
        return self.notional * (df_start - df_end)

    def pv(self):
        return self.pv_floating_leg() - self.pv_fixed_leg()

    def par_rate(self):
        denom = sum(self.curve.discount(t) for t in self.times)
        return (1 - self.curve.discount(self.times[-1])) / denom
