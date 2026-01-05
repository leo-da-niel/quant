import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from core.curves import discount_factor

st.title("Yield Curve Construction")

st.markdown(
    """
    This module illustrates the construction of a basic interest rate curve and
    its use for discounting and forward rate analysis.
    """
)

# Inputs
st.sidebar.header("Curve Inputs")

tenors = st.sidebar.multiselect(
    "Tenors (years)",
    options=[0.25, 0.5, 1, 2, 5, 10],
    default=[0.5, 1, 2, 5]
)

rates = []
for t in tenors:
    rates.append(
        st.sidebar.number_input(
            f"Zero rate for {t}Y",
            value=0.05,
            step=0.001
        )
    )

if tenors:
    df_curve = pd.DataFrame(
        {
            "Tenor (Y)": tenors,
            "Zero Rate": rates,
            "Discount Factor": [
                discount_factor(r, t) for r, t in zip(rates, tenors)
            ],
        }
    )

    st.subheader("Zero Curve")
    st.dataframe(df_curve)

    fig, ax = plt.subplots()
    ax.plot(df_curve["Tenor (Y)"], df_curve["Zero Rate"], marker="o")
    ax.set_xlabel("Tenor (Years)")
    ax.set_ylabel("Zero Rate")
    ax.set_title("Zero Rate Curve")
    st.pyplot(fig)
