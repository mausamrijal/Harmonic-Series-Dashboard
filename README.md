# Harmonic Series Dashboard (Exact Fractions)

An interactive **Streamlit dashboard** to explore the **harmonic series**

\[
H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}
\]

This app:
- Computes the sum **exactly** using rational fractions
- Automatically **reduces fractions** (e.g. `18/15 → 6/5`)
- Marks when a **reduction occurs**
- Plots the growth of \( H_n \)
- Compares it with the approximation \( \ln(n) + \gamma \)

---

## 🚀 Features

- ✅ Exact arithmetic using `fractions.Fraction`
- ✅ No floating-point errors in calculations
- 📈 Interactive graph of harmonic growth
- 📊 Comparison with logarithmic approximation
- 🧮 Table showing:
  - exact fraction
  - decimal value
  - reduction marker
- 🛡️ Safe handling of **very large integers** (Arrow/Streamlit compatible)

---

## 🧠 Why this is interesting

The harmonic series:
- **Diverges**, but very slowly
- Grows approximately like `ln(n)`
- Produces rapidly growing numerators and denominators

This dashboard makes those properties **visible and intuitive**.

---

## 📦 Requirements

- Python **3.9+** (tested on 3.13)
- Streamlit
- Pandas
- Altair (optional, for advanced plotting)

---

## 🔧 Installation

On **Windows / macOS / Linux**:

```bash
python -m pip install streamlit pandas altair

