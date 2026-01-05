import streamlit as st
import numpy as np
import pandas as pd

from core.bootstrap import bootstrap_curve
from core.curve import ZeroCurve
from derivatives.swaps import InterestRateSwap
from derivatives.swaps import bucketed_dv01

st.title("Curva de Tasas y Sensibilidades (DV01)")

st.markdown("""
Bootstrap de curva a partir de swaps par.
Interpolación log-lineal en factores de descuento.
""")

# Inputs de mercado
tenors = st.multiselect(
    "Tenores (años)",
    [0.5, 1, 2, 3, 5, 7, 10],
    default=[1, 2, 5, 10]
)

rates = []
for t in tenors:
    rates.append(
        st.number_input(f"Swap {t}Y", value=0.10 + 0.002 * t)
    )

# Bootstrap
dfs = bootstrap_curve(tenors, rates)
curve = ZeroCurve(tenors, dfs)

# Tabla curva
curve_df = pd.DataFrame({
    "Tenor": tenors,
    "Discount Factor": dfs,
    "Zero Rate": [curve.zero_rate(t) for t in tenors]
})

st.subheader("Curva Bootstrap")
st.dataframe(curve_df)

# Swap pricing
st.subheader("Swap y DV01")

notional = st.number_input("Notional", value=1_000_000)
maturity = st.selectbox("Maturity", tenors)
fixed_rate = st.number_input("Fixed Rate", value=0.12)

payment_times = [t for t in tenors if t <= maturity]

swap = InterestRateSwap(notional, fixed_rate, payment_times, curve)

st.metric("PV Swap", f"{swap.pv():,.2f}")
st.metric("DV01", f"{swap.dv01():,.2f}")

# Bucketed DV01
st.subheader("Bucketed DV01")

bucket = bucketed_dv01(curve, swap)

dv01_df = pd.DataFrame({
    "Tenor": bucket.keys(),
    "DV01": bucket.values()
})

st.bar_chart(dv01_df.set_index("Tenor"))
