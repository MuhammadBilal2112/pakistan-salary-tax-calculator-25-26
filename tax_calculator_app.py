import streamlit as st
import pandas as pd
import altair as alt

# --- Tax Calculation Functions ---

def calculate_tax_2024_25(annual_salary):
    if annual_salary <= 600000:
        return 0
    elif annual_salary <= 1200000:
        return (annual_salary - 600000) * 0.05
    elif annual_salary <= 2200000:
        return 30000 + (annual_salary - 1200000) * 0.15
    elif annual_salary <= 3200000:
        return 180000 + (annual_salary - 2200000) * 0.25
    else:
        return 430000 + (annual_salary - 3200000) * 0.30

def calculate_tax_2025_26(annual_salary):
    if annual_salary <= 600000:
        return 0
    elif annual_salary <= 1200000:
        return (annual_salary - 600000) * 0.01
    elif annual_salary <= 2200000:
        return 6000 + (annual_salary - 1200000) * 0.11
    elif annual_salary <= 3200000:
        return 126000 + (annual_salary - 2200000) * 0.23
    else:
        return 356000 + (annual_salary - 3200000) * 0.28

# --- Streamlit Page Config ---
st.set_page_config(page_title="Pakistan Tax Calculator", page_icon="💸")

# --- UI Layout ---
st.title("💸 Pakistan Salary Tax Calculator")
st.caption("Compare your income tax under 2024–25 vs 2025–26 budgets")

monthly_salary = st.number_input("Enter your Monthly Salary (PKR):", min_value=0, step=1000)

if monthly_salary > 0:
    annual_salary = monthly_salary * 12
    tax_2024 = round(calculate_tax_2024_25(annual_salary))
    tax_2025 = round(calculate_tax_2025_26(annual_salary))
    monthly_tax_2024 = round(tax_2024 / 12)
    monthly_tax_2025 = round(tax_2025 / 12)
    savings = monthly_tax_2024 - monthly_tax_2025

    st.markdown("## 📊 Tax Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📅 2024–25")
        st.metric("Annual Tax", f"Rs {tax_2024:,.0f}")
        st.metric("Monthly Tax", f"Rs {monthly_tax_2024:,.0f}")

    with col2:
        st.subheader("📅 2025–26")
        st.metric("Annual Tax", f"Rs {tax_2025:,.0f}")
        st.metric("Monthly Tax", f"Rs {monthly_tax_2025:,.0f}")

    if savings > 0:
        st.success(f"🎉 You save **Rs {savings:,.0f}** per month under the new budget!")
    elif savings < 0:
        st.warning(f"⚠️ You pay **Rs {-savings:,.0f}** more per month under the new budget.")
    else:
        st.info("ℹ️ Your monthly tax remains the same.")

    # --- Optional Chart ---
    st.markdown("### 📈 Tax by Salary Range (Visual)")
    salaries = list(range(50000, 700001, 50000))
    data = {
        "Monthly Salary": salaries,
        "Annual Salary": [s * 12 for s in salaries],
        "Tax 2024–25": [calculate_tax_2024_25(s * 12) for s in salaries],
        "Tax 2025–26": [calculate_tax_2025_26(s * 12) for s in salaries],
    }
    df = pd.DataFrame(data)

    chart = alt.Chart(df).transform_fold(
        ['Tax 2024–25', 'Tax 2025–26'],
        as_=['Budget', 'Amount']
    ).mark_line(point=True).encode(
        x=alt.X('Monthly Salary', title='Monthly Salary (PKR)'),
        y=alt.Y('Amount', title='Annual Tax (PKR)'),
        color='Budget:N'
    ).properties(width=700, height=400)

    st.altair_chart(chart, use_container_width=True)
