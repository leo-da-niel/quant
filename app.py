import streamlit as st

st.set_page_config(
    page_title="Quant Pricing & Risk Platform",
    layout="wide"
)

st.title("Quantitative Pricing & Risk Calculators")
st.subheader(
    "Interest Rate Derivatives, Volatility Surfaces, and Counterparty Credit Risk"
)

st.markdown("---")

st.markdown(
    """
    ### Overview

    This platform presents a collection of quantitative calculators focused on **interest rate products**,
    designed to reflect market-standard approaches used in pricing, risk management, and valuation adjustments.

    The objective is not to provide black-box outputs, but to **expose modeling assumptions, numerical methods,
    and sensitivities** commonly required in professional quant and risk roles.
    """
)

st.markdown(
    """
    ### Scope of the Platform

    - **Yield Curves & Discounting**  
      Curve construction, bootstrapping, interpolation, and sensitivity analysis.

    - **Interest Rate Derivatives**  
      Pricing and risk of swaps, swaptions, caps, and floors.

    - **Volatility Modeling**  
      Smile and surface construction, with emphasis on SABR-type parametrizations.

    - **Counterparty Credit Risk (CVA / XVA)**  
      Exposure profiles, expected exposure, and valuation adjustments.

    - **Structured Products**  
      Pricing of callable and path-dependent interest rate instruments.
    """
)

st.markdown(
    """
    ### Design Principles

    - Explicit financial assumptions and conventions  
    - Modular and extensible Python architecture  
    - Numerical stability over analytical shortcuts  
    - Clear separation between model logic and user interface
    """
)

st.markdown("---")

st.markdown(
    """
    **Technology Stack:**  
    Python · NumPy · SciPy · pandas · Streamlit · Monte Carlo Simulation

    **Author:**  
    Quantitative Finance Portfolio Project
    """
)
