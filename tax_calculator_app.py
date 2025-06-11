import streamlit as st

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

st.title("🇵🇰 Pakistan Salary Tax Calculator (2025–26 vs 2024–25)")

monthly_salary = st.number_input("Enter your Monthly Salary (PKR):", min_value=0, step=1000)

if monthly_salary > 0:
    annual_salary = monthly_salary * 12
    tax_2024 = round(calculate_tax_2024_25(annual_salary))
    tax_2025 = round(calculate_tax_2025_26(annual_salary))
    monthly_tax_2024 = round(tax_2024 / 12)
    monthly_tax_2025 = round(tax_2025 / 12)
    savings = monthly_tax_2024 - monthly_tax_2025

    st.markdown("### 🧾 Results")
    st.write(f"**Annual Salary:** Rs {annual_salary:,.0f}")
    st.write(f"🟠 **2024–25 Tax:** Rs {tax_2024:,.0f} annually | Rs {monthly_tax_2024:,.0f} monthly")
    st.write(f"🟢 **2025–26 Tax:** Rs {tax_2025:,.0f} annually | Rs {monthly_tax_2025:,.0f} monthly")
    st.success(f"✅ **Monthly Savings:** Rs {savings:,.0f}")
