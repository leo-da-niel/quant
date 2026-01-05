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
