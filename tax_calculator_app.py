# # # # # # import streamlit as st
# # # # # # import pandas as pd
# # # # # # import altair as alt

# # # # # # # --- Tax Calculation Functions ---

# # # # # # def calculate_tax_2024_25(annual_salary):
# # # # # #     if annual_salary <= 600000:
# # # # # #         return 0
# # # # # #     elif annual_salary <= 1200000:
# # # # # #         return (annual_salary - 600000) * 0.05
# # # # # #     elif annual_salary <= 2200000:
# # # # # #         return 30000 + (annual_salary - 1200000) * 0.15
# # # # # #     elif annual_salary <= 3200000:
# # # # # #         return 180000 + (annual_salary - 2200000) * 0.25
# # # # # #     else:
# # # # # #         return 430000 + (annual_salary - 3200000) * 0.30

# # # # # # def calculate_tax_2025_26(annual_salary):
# # # # # #     if annual_salary <= 600000:
# # # # # #         return 0
# # # # # #     elif annual_salary <= 1200000:
# # # # # #         return (annual_salary - 600000) * 0.01
# # # # # #     elif annual_salary <= 2200000:
# # # # # #         return 6000 + (annual_salary - 1200000) * 0.11
# # # # # #     elif annual_salary <= 3200000:
# # # # # #         return 126000 + (annual_salary - 2200000) * 0.23
# # # # # #     else:
# # # # # #         return 356000 + (annual_salary - 3200000) * 0.28

# # # # # # # --- Streamlit Config ---
# # # # # # st.set_page_config(page_title="Pakistan Tax Calculator", page_icon="💸")

# # # # # # # --- UI Header ---
# # # # # # st.title("💸 Pakistan Salary Tax Calculator")
# # # # # # st.caption("Compare your income tax under 2024–25 vs 2025–26 budgets")

# # # # # # # --- Salary Input ---
# # # # # # monthly_salary = st.number_input("Enter your Monthly Salary (PKR):", min_value=0, step=1000)

# # # # # # if monthly_salary > 0:
# # # # # #     annual_salary = monthly_salary * 12
# # # # # #     tax_2024 = round(calculate_tax_2024_25(annual_salary))
# # # # # #     tax_2025 = round(calculate_tax_2025_26(annual_salary))
# # # # # #     monthly_tax_2024 = round(tax_2024 / 12)
# # # # # #     monthly_tax_2025 = round(tax_2025 / 12)
# # # # # #     savings = monthly_tax_2024 - monthly_tax_2025

# # # # # #     # --- Side-by-side Comparison ---
# # # # # #     st.markdown("## 📊 Tax Comparison")
# # # # # #     col1, col2 = st.columns(2)

# # # # # #     with col1:
# # # # # #         st.subheader("📅 2024–25")
# # # # # #         st.metric("Annual Tax", f"Rs {tax_2024:,.0f}")
# # # # # #         st.metric("Monthly Tax", f"Rs {monthly_tax_2024:,.0f}")

# # # # # #     with col2:
# # # # # #         st.subheader("📅 2025–26")
# # # # # #         st.metric("Annual Tax", f"Rs {tax_2025:,.0f}")
# # # # # #         st.metric("Monthly Tax", f"Rs {monthly_tax_2025:,.0f}")

# # # # # #     # --- Feedback ---
# # # # # #     if savings > 0:
# # # # # #         st.success(f"🎉 You save **Rs {savings:,.0f}** per month under the new budget!")
# # # # # #     elif savings < 0:
# # # # # #         st.warning(f"⚠️ You pay **Rs {-savings:,.0f}** more per month under the new budget.")
# # # # # #     else:
# # # # # #         st.info("ℹ️ Your monthly tax remains the same.")

# # # # # #     # --- Visual Chart ---
# # # # # #     st.markdown("### 📈 Tax Comparison by Salary")

# # # # # #     salaries = list(range(50000, 700001, 50000))
# # # # # #     chart_data = pd.DataFrame({
# # # # # #         "Monthly Salary (PKR)": salaries,
# # # # # #         "2024–25 Tax (Annual)": [calculate_tax_2024_25(s * 12) for s in salaries],
# # # # # #         "2025–26 Tax (Annual)": [calculate_tax_2025_26(s * 12) for s in salaries],
# # # # # #     })

# # # # # #     chart = alt.Chart(chart_data).transform_fold(
# # # # # #         ["2024–25 Tax (Annual)", "2025–26 Tax (Annual)"],
# # # # # #         as_=["Budget Year", "Tax"]
# # # # # #     ).mark_line(point=True).encode(
# # # # # #         x="Monthly Salary (PKR):Q",
# # # # # #         y="Tax:Q",
# # # # # #         color="Budget Year:N"
# # # # # #     ).properties(width=700, height=400)

# # # # # #     st.altair_chart(chart, use_container_width=True)

# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import altair as alt
# # # # # import time

# # # # # # --- Tax Calculation Functions ---
# # # # # def calculate_tax_2024_25(annual_salary):
# # # # #     if annual_salary <= 600000:
# # # # #         return 0
# # # # #     elif annual_salary <= 1200000:
# # # # #         return (annual_salary - 600000) * 0.05
# # # # #     elif annual_salary <= 2200000:
# # # # #         return 30000 + (annual_salary - 1200000) * 0.15
# # # # #     elif annual_salary <= 3200000:
# # # # #         return 180000 + (annual_salary - 2200000) * 0.25
# # # # #     else:
# # # # #         return 430000 + (annual_salary - 3200000) * 0.30

# # # # # def calculate_tax_2025_26(annual_salary):
# # # # #     if annual_salary <= 600000:
# # # # #         return 0
# # # # #     elif annual_salary <= 1200000:
# # # # #         return (annual_salary - 600000) * 0.01
# # # # #     elif annual_salary <= 2200000:
# # # # #         return 6000 + (annual_salary - 1200000) * 0.11
# # # # #     elif annual_salary <= 3200000:
# # # # #         return 126000 + (annual_salary - 2200000) * 0.23
# # # # #     else:
# # # # #         return 356000 + (annual_salary - 3200000) * 0.28

# # # # # # --- Animated Counter ---
# # # # # def animate_count(label, final_value, duration=1.2):
# # # # #     container = st.empty()
# # # # #     steps = 20
# # # # #     delay = duration / steps
# # # # #     for i in range(1, steps + 1):
# # # # #         value = int(final_value * i / steps)
# # # # #         container.metric(label, f"Rs {value:,.0f}")
# # # # #         time.sleep(delay)

# # # # # # --- Page Setup ---
# # # # # st.set_page_config(page_title="Pakistan Tax Calculator", page_icon="💸")
# # # # # st.title("💸 Pakistan Salary Tax Calculator")
# # # # # st.caption("Compare your income tax under 2024–25 vs 2025–26 federal budgets.")

# # # # # # --- User Input ---
# # # # # with st.sidebar:
# # # # #     st.header("💼 Your Salary")
# # # # #     monthly_salary = st.number_input("Monthly Salary (PKR):", min_value=0, step=1000)


# # # # # # --- Tax Calculations ---
# # # # # if monthly_salary > 0:
# # # # #     annual_salary = monthly_salary * 12
# # # # #     tax_2024 = round(calculate_tax_2024_25(annual_salary))
# # # # #     tax_2025 = round(calculate_tax_2025_26(annual_salary))
# # # # #     monthly_tax_2024 = round(tax_2024 / 12)
# # # # #     monthly_tax_2025 = round(tax_2025 / 12)
# # # # #     savings = monthly_tax_2024 - monthly_tax_2025

# # # # #     st.markdown("## 📊 Tax Comparison")

# # # # #     # --- Side-by-side Layout ---
# # # # #     col1, col2 = st.columns(2)

# # # # #     with col1:
# # # # #         st.subheader("📅 2024–25")
# # # # #         animate_count("Annual Tax", tax_2024)
# # # # #         animate_count("Monthly Tax", monthly_tax_2024)

# # # # #     with col2:
# # # # #         st.subheader("📅 2025–26")
# # # # #         animate_count("Annual Tax", tax_2025)
# # # # #         animate_count("Monthly Tax", monthly_tax_2025)

# # # # #     # --- Savings Result ---
# # # # #     if savings > 0:
# # # # #         st.success(f"🎉 You save **Rs {savings:,.0f}** per month under the new budget!")
# # # # #     elif savings < 0:
# # # # #         st.warning(f"⚠️ You pay **Rs {-savings:,.0f}** more per month under the new budget.")
# # # # #     else:
# # # # #         st.info("ℹ️ Your monthly tax remains the same.")

# # # # #     # --- Tax Chart ---
# # # # #     st.markdown("### 📈 Tax Comparison by Salary")

# # # # #     salaries = list(range(50000, 700001, 50000))
# # # # #     chart_data = pd.DataFrame({
# # # # #         "Monthly Salary (PKR)": salaries,
# # # # #         "2024–25 Tax (Annual)": [calculate_tax_2024_25(s * 12) for s in salaries],
# # # # #         "2025–26 Tax (Annual)": [calculate_tax_2025_26(s * 12) for s in salaries],
# # # # #     })

# # # # #     chart = alt.Chart(chart_data).transform_fold(
# # # # #         ["2024–25 Tax (Annual)", "2025–26 Tax (Annual)"],
# # # # #         as_=["Budget Year", "Tax"]
# # # # #     ).mark_line(point=True).encode(
# # # # #         x="Monthly Salary (PKR):Q",
# # # # #         y="Tax:Q",
# # # # #         color="Budget Year:N"
# # # # #     ).properties(width=700, height=400)

# # # # #     st.altair_chart(chart, use_container_width=True)

# # # # import streamlit as st
# # # # import pandas as pd
# # # # import altair as alt
# # # # import time

# # # # # --- Tax Calculation Functions ---
# # # # def calculate_tax_2024_25(annual_salary):
# # # #     if annual_salary <= 600000:
# # # #         return 0
# # # #     elif annual_salary <= 1200000:
# # # #         return (annual_salary - 600000) * 0.05
# # # #     elif annual_salary <= 2200000:
# # # #         return 30000 + (annual_salary - 1200000) * 0.15
# # # #     elif annual_salary <= 3200000:
# # # #         return 180000 + (annual_salary - 2200000) * 0.25
# # # #     else:
# # # #         return 430000 + (annual_salary - 3200000) * 0.30

# # # # def calculate_tax_2025_26(annual_salary):
# # # #     if annual_salary <= 600000:
# # # #         return 0
# # # #     elif annual_salary <= 1200000:
# # # #         return (annual_salary - 600000) * 0.01
# # # #     elif annual_salary <= 2200000:
# # # #         return 6000 + (annual_salary - 1200000) * 0.11
# # # #     elif annual_salary <= 3200000:
# # # #         return 126000 + (annual_salary - 2200000) * 0.23
# # # #     else:
# # # #         return 356000 + (annual_salary - 3200000) * 0.28

# # # # # --- Animated Counter ---
# # # # def animate_count(label, final_value, duration=1.2):
# # # #     container = st.empty()
# # # #     steps = 20
# # # #     delay = duration / steps
# # # #     for i in range(1, steps + 1):
# # # #         value = int(final_value * i / steps)
# # # #         container.metric(label, f"Rs {value:,.0f}")
# # # #         time.sleep(delay)

# # # # # --- Page Setup ---
# # # # st.set_page_config(page_title="Pakistan Tax Calculator", page_icon="💸")
# # # # st.title("💸 Pakistan Salary Tax Calculator")
# # # # st.caption("Compare your income tax under 2024–25 vs 2025–26 federal budgets.")

# # # # # --- Sidebar Inputs ---
# # # # with st.sidebar:
# # # #     st.header("💼 Your Salary")
# # # #     monthly_salary = st.number_input("Monthly Salary (PKR):", min_value=0, step=1000)

# # # #     st.markdown("### 🔘 Try Preset Values")
# # # #     if st.button("Rs 100,000/month"):
# # # #         monthly_salary = 100000
# # # #     if st.button("Rs 250,000/month"):
# # # #         monthly_salary = 250000

# # # # # --- Info Block ---
# # # # st.markdown("""
# # # # ℹ️ This tool compares income tax based on Pakistan’s **Federal Budgets** for  
# # # # **2024–25** and **2025–26** using official tax slabs.

# # # # Just enter your salary to get started.
# # # # """)

# # # # # --- Calculations ---
# # # # if monthly_salary > 0:
# # # #     annual_salary = monthly_salary * 12
# # # #     tax_2024 = round(calculate_tax_2024_25(annual_salary))
# # # #     tax_2025 = round(calculate_tax_2025_26(annual_salary))
# # # #     monthly_tax_2024 = round(tax_2024 / 12)
# # # #     monthly_tax_2025 = round(tax_2025 / 12)
# # # #     savings = monthly_tax_2024 - monthly_tax_2025

# # # #     # --- Tabs: Results and Chart ---
# # # #     tab1, tab2 = st.tabs(["📊 Tax Comparison", "📈 Tax Chart"])

# # # #     with tab1:
# # # #         st.markdown("### 🧾 Tax Result Breakdown")

# # # #         col1, col2 = st.columns(2)

# # # #         with col1:
# # # #             st.subheader("📅 2024–25")
# # # #             animate_count("Annual Tax", tax_2024)
# # # #             animate_count("Monthly Tax", monthly_tax_2024)

# # # #         with col2:
# # # #             st.subheader("📅 2025–26")
# # # #             animate_count("Annual Tax", tax_2025)
# # # #             animate_count("Monthly Tax", monthly_tax_2025)

# # # #         if savings > 0:
# # # #             st.success(f"🎉 You save **Rs {savings:,.0f}** per month under the new budget!")
# # # #         elif savings < 0:
# # # #             st.warning(f"⚠️ You pay **Rs {-savings:,.0f}** more per month under the new budget.")
# # # #         else:
# # # #             st.info("ℹ️ Your monthly tax remains the same.")

# # # #     with tab2:
# # # #         st.markdown("### 📈 Tax vs Salary Chart")
# # # #         salaries = list(range(50000, 700001, 50000))
# # # #         chart_data = pd.DataFrame({
# # # #             "Monthly Salary (PKR)": salaries,
# # # #             "2024–25 Tax (Annual)": [calculate_tax_2024_25(s * 12) for s in salaries],
# # # #             "2025–26 Tax (Annual)": [calculate_tax_2025_26(s * 12) for s in salaries],
# # # #         })

# # # #         chart = alt.Chart(chart_data).transform_fold(
# # # #             ["2024–25 Tax (Annual)", "2025–26 Tax (Annual)"],
# # # #             as_=["Budget Year", "Tax"]
# # # #         ).mark_line(point=True).encode(
# # # #             x="Monthly Salary (PKR):Q",
# # # #             y="Tax:Q",
# # # #             color="Budget Year:N"
# # # #         ).properties(width=700, height=400)

# # # #         st.altair_chart(chart, use_container_width=True)

# # # import streamlit as st
# # # import pandas as pd
# # # import altair as alt
# # # import time

# # # # --- Tax Calculation Functions ---
# # # def calculate_tax_2024_25(annual_salary):
# # #     if annual_salary <= 600000:
# # #         return 0
# # #     elif annual_salary <= 1200000:
# # #         return (annual_salary - 600000) * 0.05
# # #     elif annual_salary <= 2200000:
# # #         return 30000 + (annual_salary - 1200000) * 0.15
# # #     elif annual_salary <= 3200000:
# # #         return 180000 + (annual_salary - 2200000) * 0.25
# # #     else:
# # #         return 430000 + (annual_salary - 3200000) * 0.30

# # # def calculate_tax_2025_26(annual_salary):
# # #     if annual_salary <= 600000:
# # #         return 0
# # #     elif annual_salary <= 1200000:
# # #         return (annual_salary - 600000) * 0.01
# # #     elif annual_salary <= 2200000:
# # #         return 6000 + (annual_salary - 1200000) * 0.11
# # #     elif annual_salary <= 3200000:
# # #         return 126000 + (annual_salary - 2200000) * 0.23
# # #     else:
# # #         return 356000 + (annual_salary - 3200000) * 0.28

# # # # --- Animated Counter ---
# # # def animate_count(label, final_value, duration=1.2):
# # #     container = st.empty()
# # #     steps = 20
# # #     delay = duration / steps
# # #     for i in range(1, steps + 1):
# # #         value = int(final_value * i / steps)
# # #         container.metric(label, f"Rs {value:,.0f}")
# # #         time.sleep(delay)

# # # # --- Page Config ---
# # # st.set_page_config(page_title="Pakistan Tax Calculator", page_icon="💸")

# # # # --- Sidebar Input ---
# # # with st.sidebar:
# # #     st.header("💼 Your Salary")

# # #     monthly_salary = st.number_input("Monthly Salary (PKR):", min_value=0, step=1000)

# # #     st.markdown("### 🔘 Try Preset Values")
# # #     if st.button("Rs 100,000/month"):
# # #         monthly_salary = 100000
# # #     if st.button("Rs 250,000/month"):
# # #         monthly_salary = 250000

# # #     theme = st.radio("Theme", ["🌞 Light", "🌙 Dark"])

# # #     if theme == "🌙 Dark":
# # #         st.markdown(
# # #             """
# # #             <style>
# # #             body {
# # #                 background-color: #0e1117 !important;
# # #                 color: #FAFAFA !important;
# # #             }
# # #             .stApp {
# # #                 background-color: #0e1117 !important;
# # #                 color: #FAFAFA !important;
# # #             }
# # #             .css-1d391kg, .css-1v3fvcr, .css-1avcm0n {
# # #                 background-color: #1e1e1e !important;
# # #             }
# # #             .css-ffhzg2 {
# # #                 color: #FAFAFA !important;
# # #             }
# # #             </style>
# # #             """,
# # #             unsafe_allow_html=True,
# # #         )
# # #     else:
# # #         st.markdown(
# # #             """
# # #             <style>
# # #             body {
# # #                 background-color: white !important;
# # #                 color: black !important;
# # #             }
# # #             .stApp {
# # #                 background-color: white !important;
# # #                 color: black !important;
# # #             }
# # #             </style>
# # #             """,
# # #             unsafe_allow_html=True,
# # #         )

    

# # #     # theme = st.radio("Theme", ["🌞 Light", "🌙 Dark"])
# # #     # if theme == "🌙 Dark":
# # #     #     st.markdown(
# # #     #         """
# # #     #         <style>
# # #     #         html, body, [class*="css"] {

# # #     #             background-color: #0e1117 !important;
# # #     #             color: #FAFAFA !important;
# # #     #         }
# # #     #         </style>
# # #     #         """,
# # #     #         unsafe_allow_html=True,
# # #     #     )

# # # # --- Main Title and Info ---
# # # st.title("💸 Pakistan Salary Tax Calculator")
# # # st.caption("Compare your income tax under 2024–25 vs 2025–26 federal budgets.")

# # # st.markdown("""
# # # ℹ️ This tool compares income tax based on Pakistan’s **Federal Budgets** for  
# # # **2024-25** and **2025-26** using official tax slabs.
# # # """)

# # # # --- Tax Logic ---
# # # if monthly_salary > 0:
# # #     annual_salary = monthly_salary * 12
# # #     tax_2024 = round(calculate_tax_2024_25(annual_salary))
# # #     tax_2025 = round(calculate_tax_2025_26(annual_salary))
# # #     monthly_tax_2024 = round(tax_2024 / 12)
# # #     monthly_tax_2025 = round(tax_2025 / 12)
# # #     savings = monthly_tax_2024 - monthly_tax_2025

# # #     effective_rate_2024 = round((tax_2024 / annual_salary) * 100, 2)
# # #     effective_rate_2025 = round((tax_2025 / annual_salary) * 100, 2)

# # #     # --- Tabs Layout ---
# # #     tab1, tab2 = st.tabs(["📊 Tax Breakdown", "📈 Tax Chart"])

# # #     with tab1:
# # #         st.markdown("### 🧾 Comparison Details")

# # #         col1, col2 = st.columns(2)
# # #         with col1:
# # #             st.subheader("📅 2024-25")
# # #             animate_count("Annual Tax", tax_2024)
# # #             animate_count("Monthly Tax", monthly_tax_2024)
# # #             st.metric("Effective Tax Rate", f"{effective_rate_2024:.2f}%")

# # #         with col2:
# # #             st.subheader("📅 2025-26")
# # #             animate_count("Annual Tax", tax_2025)
# # #             animate_count("Monthly Tax", monthly_tax_2025)
# # #             st.metric("Effective Tax Rate", f"{effective_rate_2025:.2f}%")

# # #         if savings > 0:
# # #             st.success(f"🎉 You save **Rs {savings:,.0f}** per month under the new budget!")
# # #         elif savings < 0:
# # #             st.warning(f"⚠️ You pay **Rs {-savings:,.0f}** more per month under the new budget.")
# # #         else:
# # #             st.info("ℹ️ Your monthly tax remains the same.")

# # #     with tab2:
# # #         st.markdown("### 📈 Tax vs Salary Chart")

# # #         # Create salary range and calculate taxes
# # #         salaries = list(range(50000, 2000001, 100000))
# # #         chart_df = pd.DataFrame({
# # #             "Monthly Salary (PKR)": salaries,
# # #             "2024-25": [calculate_tax_2024_25(s * 12) for s in salaries],
# # #             "2025-26": [calculate_tax_2025_26(s * 12) for s in salaries],
# # #         })

# # #         chart = alt.Chart(chart_df).transform_fold(
# # #             ["2024-25", "2025-26"],
# # #             as_=["Budget Year", "Annual Tax"]
# # #         ).mark_line(point=True).encode(
# # #             x=alt.X("Monthly Salary (PKR):Q", title="Monthly Salary (PKR)"),
# # #             y=alt.Y("Annual Tax:Q", title="Annual Tax (PKR)"),
# # #             color="Budget Year:N",
# # #             tooltip=["Monthly Salary (PKR):Q", "Annual Tax:Q", "Budget Year:N"]
# # #         ).properties(
# # #             width=700,
# # #             height=400,
# # #             title="Annual Tax vs Salary"
# # #         )

# # #         st.altair_chart(chart, use_container_width=True)
# # import streamlit as st
# # import pandas as pd
# # import altair as alt
# # import time

# # # --- Tax Calculation Functions ---
# # def calculate_tax_2024_25(annual_salary):
# #     if annual_salary <= 600000:
# #         return 0
# #     elif annual_salary <= 1200000:
# #         return (annual_salary - 600000) * 0.05
# #     elif annual_salary <= 2200000:
# #         return 30000 + (annual_salary - 1200000) * 0.15
# #     elif annual_salary <= 3200000:
# #         return 180000 + (annual_salary - 2200000) * 0.25
# #     else:
# #         return 430000 + (annual_salary - 3200000) * 0.30

# # def calculate_tax_2025_26(annual_salary):
# #     if annual_salary <= 600000:
# #         return 0
# #     elif annual_salary <= 1200000:
# #         return (annual_salary - 600000) * 0.01
# #     elif annual_salary <= 2200000:
# #         return 6000 + (annual_salary - 1200000) * 0.11
# #     elif annual_salary <= 3200000:
# #         return 126000 + (annual_salary - 2200000) * 0.23
# #     else:
# #         return 356000 + (annual_salary - 3200000) * 0.28

# # # --- Animated Counter ---
# # def animate_count(label, final_value, duration=1.2):
# #     container = st.empty()
# #     steps = 20
# #     delay = duration / steps
# #     for i in range(1, steps + 1):
# #         value = int(final_value * i / steps)
# #         container.metric(label, f"Rs {value:,.0f}")
# #         time.sleep(delay)

# # # --- Page Setup ---
# # st.set_page_config(page_title="Pakistan Tax Calculator", page_icon="💸")

# # # --- Sidebar Salary Input ---
# # with st.sidebar:
# #     st.header("💼 Your Salary")

# #     # Initialize synced session state
# #     if "salary_input" not in st.session_state:
# #         st.session_state.salary_input = 0
# #     if "salary_slider" not in st.session_state:
# #         st.session_state.salary_slider = 0

# #     def update_slider():
# #         st.session_state.salary_slider = st.session_state.salary_input

# #     def update_input():
# #         st.session_state.salary_input = st.session_state.salary_slider

# #     st.slider(
# #         "Monthly Salary (PKR):",
# #         min_value=0,
# #         max_value=2000000,
# #         step=10000,
# #         key="salary_slider",
# #         on_change=update_input
# #     )

# #     st.number_input(
# #         "Or enter manually:",
# #         min_value=0,
# #         step=1000,
# #         key="salary_input",
# #         on_change=update_slider
# #     )

# #     monthly_salary = st.session_state.salary_input

# # # --- Title ---
# # st.title("💸 Pakistan Salary Tax Calculator")
# # st.caption("Compare your income tax under 2024–25 vs 2025–26 federal budgets.")

# # st.markdown("""
# # ℹ️ This tool compares income tax based on Pakistan’s **Federal Budgets** for  
# # **2024-25** and **2025-26** using official tax slabs.
# # """)

# # # --- Main Tax Logic ---
# # if monthly_salary > 0:
# #     annual_salary = monthly_salary * 12
# #     tax_2024 = round(calculate_tax_2024_25(annual_salary))
# #     tax_2025 = round(calculate_tax_2025_26(annual_salary))

# #     monthly_tax_2024 = round(tax_2024 / 12)
# #     monthly_tax_2025 = round(tax_2025 / 12)

# #     net_2024 = annual_salary - tax_2024
# #     net_2025 = annual_salary - tax_2025

# #     savings = monthly_tax_2024 - monthly_tax_2025

# #     rate_2024 = round((tax_2024 / annual_salary) * 100, 2)
# #     rate_2025 = round((tax_2025 / annual_salary) * 100, 2)

# #     tab1, tab2 = st.tabs(["📊 Tax Breakdown", "📈 Tax Chart"])

# #     with tab1:
# #         st.markdown("### 🧾 Detailed Breakdown")

# #         col1, col2 = st.columns(2)
# #         with col1:
# #             st.subheader("📅 2024-25")
# #             animate_count("Annual Tax", tax_2024)
# #             animate_count("Monthly Tax", monthly_tax_2024)
# #             st.metric("Effective Tax Rate", f"{rate_2024:.2f}%")
# #             st.metric("Net Annual Income", f"Rs {net_2024:,.0f}")
# #             st.progress(rate_2024 / 100)

# #         with col2:
# #             st.subheader("📅 2025-26")
# #             animate_count("Annual Tax", tax_2025)
# #             animate_count("Monthly Tax", monthly_tax_2025)
# #             st.metric("Effective Tax Rate", f"{rate_2025:.2f}%")
# #             st.metric("Net Annual Income", f"Rs {net_2025:,.0f}")
# #             st.progress(rate_2025 / 100)

# #         if savings > 0:
# #             st.success(f"🎉 You save **Rs {savings:,.0f}** per month under the new budget!")
# #         elif savings < 0:
# #             st.warning(f"⚠️ You pay **Rs {-savings:,.0f}** more per month under the new budget.")
# #         else:
# #             st.info("ℹ️ Your monthly tax remains the same.")

# #     with tab2:
# #         st.markdown("### 📈 Tax vs Salary Chart")

# #         salaries = list(range(50000, 2000001, 100000))
# #         chart_data = pd.DataFrame({
# #             "Monthly Salary (PKR)": salaries,
# #             "2024-25": [calculate_tax_2024_25(s * 12) for s in salaries],
# #             "2025-26": [calculate_tax_2025_26(s * 12) for s in salaries],
# #         })

# #         chart = alt.Chart(chart_data).transform_fold(
# #             ["2024-25", "2025-26"],
# #             as_=["Budget Year", "Annual Tax"]
# #         ).mark_line(point=True).encode(
# #             x=alt.X("Monthly Salary (PKR):Q", title="Monthly Salary (PKR)"),
# #             y=alt.Y("Annual Tax:Q", title="Annual Tax (PKR)"),
# #             color="Budget Year:N",
# #             tooltip=["Monthly Salary (PKR):Q", "Annual Tax:Q", "Budget Year:N"]
# #         ).properties(width=700, height=400)

# #         st.altair_chart(chart, use_container_width=True)

# import streamlit as st
# import pandas as pd
# import altair as alt
# import time

# # --- Tax Calculation Functions ---
# def calculate_tax_2024_25(annual_salary):
#     if annual_salary <= 600000:
#         return 0
#     elif annual_salary <= 1200000:
#         return (annual_salary - 600000) * 0.05
#     elif annual_salary <= 2200000:
#         return 30000 + (annual_salary - 1200000) * 0.15
#     elif annual_salary <= 3200000:
#         return 180000 + (annual_salary - 2200000) * 0.25
#     else:
#         return 430000 + (annual_salary - 3200000) * 0.30

# def calculate_tax_2025_26(annual_salary):
#     if annual_salary <= 600000:
#         return 0
#     elif annual_salary <= 1200000:
#         return (annual_salary - 600000) * 0.01
#     elif annual_salary <= 2200000:
#         return 6000 + (annual_salary - 1200000) * 0.11
#     elif annual_salary <= 3200000:
#         return 126000 + (annual_salary - 2200000) * 0.23
#     else:
#         return 356000 + (annual_salary - 3200000) * 0.28

# # --- Animated Counter ---
# def animate_count(label, final_value, duration=1.2):
#     container = st.empty()
#     steps = 20
#     delay = duration / steps
#     for i in range(1, steps + 1):
#         value = int(final_value * i / steps)
#         container.metric(label, f"Rs {value:,.0f}")
#         time.sleep(delay)

# # --- Page Setup ---
# st.set_page_config(page_title="Pakistan Tax Calculator", page_icon="💸")

# # --- Sidebar ---
# with st.sidebar:
#     st.header("💼 Your Salary")

#     # Session state setup for synced slider and input
#     if "salary_input" not in st.session_state:
#         st.session_state.salary_input = 0
#     if "salary_slider" not in st.session_state:
#         st.session_state.salary_slider = 0

#     def update_slider():
#         st.session_state.salary_slider = st.session_state.salary_input

#     def update_input():
#         st.session_state.salary_input = st.session_state.salary_slider

#     st.slider(
#         "Monthly Salary (PKR):",
#         min_value=0,
#         max_value=2000000,
#         step=10000,
#         key="salary_slider",
#         on_change=update_input
#     )

#     st.number_input(
#         "Or enter manually:",
#         min_value=0,
#         step=1000,
#         key="salary_input",
#         on_change=update_slider
#     )

#     monthly_salary = st.session_state.salary_input

#     # --- Tax Slabs Viewer ---
#     with st.expander("📄 View Official Tax Slabs"):
#         st.markdown("#### 2024–25 Tax Slabs")
#         st.markdown("""
#         - **0 – 600,000**: No tax  
#         - **600,001 – 1,200,000**: 5% of amount over 600,000  
#         - **1,200,001 – 2,200,000**: Rs 30,000 + 15% of amount over 1,200,000  
#         - **2,200,001 – 3,200,000**: Rs 180,000 + 25% of amount over 2,200,000  
#         - **3,200,001 and above**: Rs 430,000 + 30% of amount over 3,200,000
#         """)

#         st.markdown("#### 2025–26 Tax Slabs")
#         st.markdown("""
#         - **0 – 600,000**: No tax  
#         - **600,001 – 1,200,000**: 1% of amount over 600,000  
#         - **1,200,001 – 2,200,000**: Rs 6,000 + 11% of amount over 1,200,000  
#         - **2,200,001 – 3,200,000**: Rs 126,000 + 23% of amount over 2,200,000  
#         - **3,200,001 and above**: Rs 356,000 + 28% of amount over 3,200,000
#         """)

# # --- Main UI ---
# st.title("💸 Pakistan Salary Tax Calculator")
# st.caption("Compare your income tax under 2024–25 vs 2025–26 federal budgets.")

# st.markdown("""
# ℹ️ This tool compares income tax based on Pakistan’s **Federal Budgets** for  
# **2024-25** and **2025-26** using official tax slabs.
# """)

# # --- Main Logic ---
# if monthly_salary > 0:
#     annual_salary = monthly_salary * 12
#     tax_2024 = round(calculate_tax_2024_25(annual_salary))
#     tax_2025 = round(calculate_tax_2025_26(annual_salary))

#     monthly_tax_2024 = round(tax_2024 / 12)
#     monthly_tax_2025 = round(tax_2025 / 12)

#     net_2024 = annual_salary - tax_2024
#     net_2025 = annual_salary - tax_2025

#     savings = monthly_tax_2024 - monthly_tax_2025

#     rate_2024 = round((tax_2024 / annual_salary) * 100, 2)
#     rate_2025 = round((tax_2025 / annual_salary) * 100, 2)

#     tab1, tab2 = st.tabs(["📊 Tax Breakdown", "📈 Tax Chart"])

#     with tab1:
#         st.markdown("### 🧾 Detailed Breakdown")

#         col1, col2 = st.columns(2)
#         with col1:
#             st.subheader("📅 2024-25")
#             animate_count("Annual Tax", tax_2024)
#             animate_count("Monthly Tax", monthly_tax_2024)
#             st.metric("Effective Tax Rate", f"{rate_2024:.2f}%")
#             st.metric("Net Annual Income", f"Rs {net_2024:,.0f}")
#             st.metric("Net Monthly Income", f"Rs {net_2024 // 12:,.0f}")
#             st.progress(rate_2024 / 100)

#         with col2:
#             st.subheader("📅 2025-26")
#             animate_count("Annual Tax", tax_2025)
#             animate_count("Monthly Tax", monthly_tax_2025)
#             st.metric("Effective Tax Rate", f"{rate_2025:.2f}%")
#             st.metric("Net Annual Income", f"Rs {net_2025:,.0f}")
#             st.metric("Net Monthly Income", f"Rs {net_2025 // 12:,.0f}")
#             st.progress(rate_2025 / 100)

#         if savings > 0:
#             st.success(f"🎉 You save **Rs {savings:,.0f}** per month under the new budget!")
#         elif savings < 0:
#             st.warning(f"⚠️ You pay **Rs {-savings:,.0f}** more per month under the new budget.")
#         else:
#             st.info("ℹ️ Your monthly tax remains the same.")

#     with tab2:
#         st.markdown("### 📈 Tax vs Salary Chart")

#         salaries = list(range(50000, 2000001, 100000))
#         chart_data = pd.DataFrame({
#             "Monthly Salary (PKR)": salaries,
#             "2024-25": [calculate_tax_2024_25(s * 12) for s in salaries],
#             "2025-26": [calculate_tax_2025_26(s * 12) for s in salaries],
#         })

#         chart = alt.Chart(chart_data).transform_fold(
#             ["2024-25", "2025-26"],
#             as_=["Budget Year", "Annual Tax"]
#         ).mark_line(point=True).encode(
#             x=alt.X("Monthly Salary (PKR):Q", title="Monthly Salary (PKR)"),
#             y=alt.Y("Annual Tax:Q", title="Annual Tax (PKR)"),
#             color="Budget Year:N",
#             tooltip=["Monthly Salary (PKR):Q", "Annual Tax:Q", "Budget Year:N"]
#         ).properties(width=700, height=400)

#         st.altair_chart(chart, use_container_width=True)
import streamlit as st
import pandas as pd
import altair as alt
import time

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

# --- Animated Counter ---
def animate_count(label, final_value, duration=1.2):
    container = st.empty()
    steps = 20
    delay = duration / steps
    for i in range(1, steps + 1):
        value = int(final_value * i / steps)
        container.metric(label, f"Rs {value:,.0f}")
        time.sleep(delay)

# --- Page Setup ---
st.set_page_config(page_title="Pakistan Tax Calculator", page_icon="💸")

# --- Sidebar ---
with st.sidebar:
    st.header("💼 Your Salary")

    # Session state setup for synced slider and input
    if "salary_input" not in st.session_state:
        st.session_state.salary_input = 0
    if "salary_slider" not in st.session_state:
        st.session_state.salary_slider = 0

    def update_slider():
        st.session_state.salary_slider = st.session_state.salary_input

    def update_input():
        st.session_state.salary_input = st.session_state.salary_slider

    st.slider(
        "Monthly Salary (PKR):",
        min_value=0,
        max_value=2000000,
        step=10000,
        key="salary_slider",
        on_change=update_input
    )

    st.number_input(
        "Or enter manually:",
        min_value=0,
        step=1000,
        key="salary_input",
        on_change=update_slider
    )

    monthly_salary = st.session_state.salary_input

    # --- Tax Slabs Viewer ---
    with st.expander("📄 View Official Tax Slabs"):
        st.markdown("#### 2024–25 Tax Slabs")
        st.markdown("""
        - **0 – 600,000**: No tax  
        - **600,001 – 1,200,000**: 5% of amount over 600,000  
        - **1,200,001 – 2,200,000**: Rs 30,000 + 15% of amount over 1,200,000  
        - **2,200,001 – 3,200,000**: Rs 180,000 + 25% of amount over 2,200,000  
        - **3,200,001 and above**: Rs 430,000 + 30% of amount over 3,200,000
        """)

        st.markdown("#### 2025–26 Tax Slabs")
        st.markdown("""
        - **0 – 600,000**: No tax  
        - **600,001 – 1,200,000**: 1% of amount over 600,000  
        - **1,200,001 – 2,200,000**: Rs 6,000 + 11% of amount over 1,200,000  
        - **2,200,001 – 3,200,000**: Rs 126,000 + 23% of amount over 2,200,000  
        - **3,200,001 and above**: Rs 356,000 + 28% of amount over 3,200,000
        """)

# --- Main UI ---
st.title("💸 Pakistan Salary Tax Calculator")
st.caption("Compare your income tax under 2024–25 vs 2025–26 federal budgets.")

st.markdown("""
ℹ️ This tool compares income tax based on Pakistan’s **Federal Budgets** for  
**2024-25** and **2025-26** using official tax slabs.
""")

# --- Main Logic ---
if monthly_salary > 0:
    annual_salary = monthly_salary * 12
    tax_2024 = round(calculate_tax_2024_25(annual_salary))
    tax_2025 = round(calculate_tax_2025_26(annual_salary))

    monthly_tax_2024 = round(tax_2024 / 12)
    monthly_tax_2025 = round(tax_2025 / 12)

    net_2024 = annual_salary - tax_2024
    net_2025 = annual_salary - tax_2025

    savings = monthly_tax_2024 - monthly_tax_2025

    rate_2024 = round((tax_2024 / annual_salary) * 100, 2)
    rate_2025 = round((tax_2025 / annual_salary) * 100, 2)

    tab1, tab2 = st.tabs(["📊 Tax Breakdown", "📈 Tax Chart"])

    with tab1:
        st.markdown("### 🧾 Detailed Breakdown")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📅 2024-25")
            animate_count("Annual Tax", tax_2024)
            animate_count("Monthly Tax", monthly_tax_2024)
            st.metric("Effective Tax Rate", f"{rate_2024:.2f}%")
            st.metric("Net Annual Income", f"Rs {net_2024:,.0f}")
            st.metric("Net Monthly Income", f"Rs {net_2024 // 12:,.0f}")
            st.progress(rate_2024 / 100)

        with col2:
            st.subheader("📅 2025-26")
            animate_count("Annual Tax", tax_2025)
            animate_count("Monthly Tax", monthly_tax_2025)
            st.metric("Effective Tax Rate", f"{rate_2025:.2f}%")
            st.metric("Net Annual Income", f"Rs {net_2025:,.0f}")
            st.metric("Net Monthly Income", f"Rs {net_2025 // 12:,.0f}")
            st.progress(rate_2025 / 100)

        if savings > 0:
            st.success(f"🎉 You save **Rs {savings:,.0f}** per month under the new budget!")
        elif savings < 0:
            st.warning(f"⚠️ You pay **Rs {-savings:,.0f}** more per month under the new budget.")
        else:
            st.info("ℹ️ Your monthly tax remains the same.")

    with tab2:
        st.markdown("### 📈 Tax & Net Income Charts")

        salaries = list(range(50000, 2000001, 100000))
        annual_salaries = [s * 12 for s in salaries]

        tax_data = pd.DataFrame({
            "Monthly Salary (PKR)": salaries,
            "2024-25 Tax (Annual)": [calculate_tax_2024_25(s) for s in annual_salaries],
            "2025-26 Tax (Annual)": [calculate_tax_2025_26(s) for s in annual_salaries],
            "2024-25 Net Income": [s - calculate_tax_2024_25(s) for s in annual_salaries],
            "2025-26 Net Income": [s - calculate_tax_2025_26(s) for s in annual_salaries],
        })

        # Chart 1: Annual Tax
        st.subheader("📉 Annual Tax vs Salary")
        tax_chart = alt.Chart(tax_data).transform_fold(
            ["2024-25 Tax (Annual)", "2025-26 Tax (Annual)"],
            as_=["Budget Year", "Tax"]
        ).mark_line(point=True).encode(
            x="Monthly Salary (PKR):Q",
            y=alt.Y("Tax:Q", title="Annual Tax (PKR)"),
            color="Budget Year:N",
            tooltip=["Monthly Salary (PKR):Q", "Tax:Q", "Budget Year:N"]
        ).properties(width=700, height=400)

        st.altair_chart(tax_chart, use_container_width=True)

        # Chart 2: Net Income
        st.subheader("💰 Net Annual Income vs Salary")
        net_chart = alt.Chart(tax_data).transform_fold(
            ["2024-25 Net Income", "2025-26 Net Income"],
            as_=["Budget Year", "Net Income"]
        ).mark_line(point=True).encode(
            x="Monthly Salary (PKR):Q",
            y=alt.Y("Net Income:Q", title="Net Annual Income (PKR)"),
            color="Budget Year:N",
            tooltip=["Monthly Salary (PKR):Q", "Net Income:Q", "Budget Year:N"]
        ).properties(width=700, height=400)

        st.altair_chart(net_chart, use_container_width=True)
