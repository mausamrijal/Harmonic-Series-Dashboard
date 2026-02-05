import math
from fractions import Fraction
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Harmonic Series Dashboard", layout="wide")
st.title("Harmonic Series Dashboard")

N = st.slider("Max n", 1, 500, 50)

harm = Fraction(0, 1)
rows = []

for n in range(1, N + 1):
    a, b = harm.numerator, harm.denominator
    before_num = a * n + b
    before_den = b * n

    harm = harm + Fraction(1, n)  # reduced automatically
    reduced = (before_num, before_den) != (harm.numerator, harm.denominator)

    rows.append({
        "n": n,
        "H_n (fraction)": f"{harm.numerator}/{harm.denominator}" if harm.denominator != 1 else str(harm.numerator),
        "H_n (decimal)": float(harm),
        "Reduced?": "YES" if reduced else "NO",

        # 👇 store BIG numbers as strings to avoid pyarrow overflow
        "Numerator": str(harm.numerator),
        "Denominator": str(harm.denominator),
        "Before (raw)": f"{before_num}/{before_den}",
    })

df = pd.DataFrame(rows)

# Plot
st.subheader("Graph")
gamma = 0.5772156649015329
plot_df = pd.DataFrame({
    "n": df["n"],
    "H_n": df["H_n (decimal)"],
    "ln(n)+γ": df["n"].apply(lambda x: math.log(x) + gamma),
}).set_index("n")

st.line_chart(plot_df)

# Table (Arrow-safe)
st.subheader("Exact Values Table (Arrow-safe)")
st.dataframe(df, use_container_width=True, height=420)
